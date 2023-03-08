from django.db import models

# Create your models here.


class Student(models.Model):
   roll_num = models.CharField(max_length=50,unique=True)
   name = models.CharField(max_length=100)
   dob = models.DateField()

   def __str__(self):
       return self.roll_num


class Marks(models.Model):
   roll_num = models.ForeignKey(Student,on_delete=models.CASCADE)
   mark = models.IntegerField()


   def __str__(self):
       return self.roll_num

