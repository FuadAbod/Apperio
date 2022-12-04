from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Homework, submitAssignment
from .serializer import HomeworkSerializer, SubmitHWSerilizaer

@api_view(['GET'])
def get_homework(request):
    if request.method == 'GET':
        homeworks = Homework.objects.all()
        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def submit_homework(request):
    if request.method == 'POST':
        data = {
            'assignment_name': request.data.get('assignment_name'),
            'student_name':request.data.get('student_name'),
            'submission_date':request.data.get('submission_date'),
            'file_attachement':request.data.get('file_attachement')
        }
        serializer = SubmitHWSerilizaer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
