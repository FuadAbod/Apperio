from django.test import TestCase
from rest_framework.test import APITestCase, APIClient

from ..models import homework
import datetime
from ..serializer import HomeworkSerializer
from rest_framework import status

class homework_object(TestCase):
    
    def setUp(self):
        homework.objects.create(
            assignment_name="LOTR",
            student_name="Alex",
            submission_date = datetime.datetime.now(),
            grading_date_time = datetime.datetime.now(),
            final_grade = 78.9
        )

    def test_homework_object(self):
        get_student_name = homework.objects.get(student_name="Alex")
        self.assertEqual(type(get_student_name.assignment_name),str)
        self.assertEqual(type(get_student_name.submission_date),datetime.date)
        self.assertEqual(type(get_student_name.grading_date_time),datetime.date)
        self.assertEqual(type(get_student_name.final_grade),float)

    def test_drf_homework_api(self):
        client = APIClient()
        response = client.get('/api/homework/')
        homeworks = homework.objects.all()
        serializer = HomeworkSerializer(homeworks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)