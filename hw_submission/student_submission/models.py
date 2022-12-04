from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(models.Model):
    student_name=models.CharField(primary_key=True,max_length=100)

class Homework(models.Model):
    assignment_name = models.CharField(max_length=100)
    student_name = models.ForeignKey(Student,on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now_add=True)
    grading_date_time = models.DateField(auto_now=True)
    file_attachement = models.ImageField(upload_to='Assignment')
    final_grade = models.FloatField()
    teachers_notes = models.CharField(max_length=1000, default='reenter')

class submitAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(
        Homework, on_delete=models.SET_NULL, blank=True, null=True)
    grade = models.FloatField()