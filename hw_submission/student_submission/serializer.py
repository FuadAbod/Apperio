from rest_framework import serializers
from .models import Homework, submitAssignment


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('assignment_name', 'student_name', 'submission_date', 'grading_date_time', 'file_attachement', 'final_grade','teachers_notes')
        # ordering = ["-final_grade"]

class SubmitHWSerilizaer(serializers.ModelSerializer):
    class Meta:
        model = submitAssignment
        fields = ('assignment_name', 'student_name', 'submission_date', 'file_attachement')

