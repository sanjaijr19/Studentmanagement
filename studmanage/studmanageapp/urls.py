
from django.urls import path
from rest_framework import routers
from .views import StudentViewSet,MarksViewSet,StudentReportView
from . import views

router =routers.DefaultRouter()



urlpatterns = [
    path('student/', views.StudentViewSet.as_view(actions={'get': 'list'}), name='student'),
    path('student/add/', views.StudentViewSet.as_view(actions={'post': 'create'}), name='student'),
    path('student/<id>/', views.StudentViewSet.as_view(actions={'get': 'retrieve'}), name='student'),
    path('student/<id>/add-mark/', views.MarksViewSet.as_view(actions={'post': 'create'}), name='marks'),
    path('mark/<id>/', views.MarksViewSet.as_view(actions={'get': 'retrieve'}), name='marks'),
    path('results/', StudentReportView.as_view() ,name='StudentReportView'),
]+router.urls