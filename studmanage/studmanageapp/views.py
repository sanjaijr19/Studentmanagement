from django.shortcuts import render
from .models import Student,Marks
from rest_framework import viewsets,generics
from .serializer import StudentSerializer,MarkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer
    lookup_field = 'id'






class StudentReportView(APIView):
    def get(self, request, format=None):
        Mark = Marks.objects.all()
        s_grade = a_grade = b_grade= c_grade = d_grade = e_grade = f_grade = 0
        total_marks = 0

        for student in Mark:
            if student.mark >= 91:
                s_grade += 1
            elif student.mark >= 81:
                a_grade += 1
            elif student.mark >= 71:
                b_grade += 1
            elif student.mark >= 61:
                c_grade += 1
            elif student.mark >= 51:
                d_grade += 1
            elif student.mark >= 50:
                e_grade += 1
            else:
                f_grade += 1

            total_marks += student.mark

        pass_percentage = ((len(Mark) - f_grade) / len(Mark)) * 100

        report = {
            "S grade": s_grade,
            "A grade": a_grade,
            "B grade": b_grade,
            "C grade": c_grade,
            "D grade": d_grade,
            "E grade": e_grade,
            "F grade": f_grade,
            "Pass Percentage": pass_percentage
        }

        return Response(report)
