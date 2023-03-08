from rest_framework import serializers
from .models import Student,Marks



class StudentSerializer(serializers.Serializer):
    roll_num = serializers.CharField()
    name = serializers.CharField()
    dob = serializers.DateField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.roll_num = validated_data.get('roll_num', instance.roll_num)
        instance.name = validated_data.get('name', instance.name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()
        return instance


class MarkSerializer(serializers.Serializer):
    roll_num = serializers.SlugRelatedField(many=False, slug_field="roll_num", queryset=Student.objects.all())
    mark = serializers.IntegerField()

    class Meta:
        model = Marks
        fields = ['roll_num','mark']


    def create(self, validated_data):
        return Marks.objects.create(**validated_data)