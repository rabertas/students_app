import datetime
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Student
from ..serializers import StudentDetailSerializer


# initialize test APIClient
client = Client()


class GetAllStudentsTest(TestCase):
    """ Test case for GET all records of Student API """

    def setUp(self):
        Student.objects.create(
            first_name='first_name2',
            surname='surname2',
            last_name='last_name2',
            date_of_birth=datetime.date(month=2, year=1992, day=2),
            grade=2
        )
        Student.objects.create(
            first_name='first_name3',
            surname='surname3',
            last_name='last_name3',
            date_of_birth=datetime.date(month=3, year=1993, day=3),
            grade=3
        )
        Student.objects.create(
            first_name='first_name4',
            surname='surname4',
            last_name='last_name4',
            date_of_birth=datetime.date(month=4, year=1994, day=4),
            grade=4
        )
        Student.objects.create(
            first_name='first_name5',
            surname='surname5',
            last_name='last_name5',
            date_of_birth=datetime.date(month=5, year=1995, day=5),
            grade=5
        )

    def test_get_all_students(self):
        # getting API data response
        response = client.get(reverse('list_endpoint'))
        # getting internal storage data
        students = Student.objects.all()
        serializer = StudentDetailSerializer(students, many=True)
        # checking success response HTTP-status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # comparing received datasets
        self.assertEqual(response.data, serializer.data)


class GetSingleStudentTest(TestCase):
    """ Test case for GET single record of Student """

    def setUp(self):
        self.student2 = Student.objects.create(
            first_name='first_name3',
            surname='surname3',
            last_name='last_name3',
            date_of_birth=datetime.date(month=3, year=1993, day=3),
            grade=3
        )
        self.student4 = Student.objects.create(
            first_name='first_name5',
            surname='surname5',
            last_name='last_name5',
            date_of_birth=datetime.date(month=5, year=1995, day=5),
            grade=5
        )

    def test_get_valid_single_experiment(self):
        response = client.get(
            reverse('records_endpoint', kwargs={'pk': self.student2.pk}))
        student2 = Student.objects.get(pk=self.student2.pk)
        serializer = StudentDetailSerializer(student2)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_experiment(self):
        response = client.get(
            reverse('records_endpoint', kwargs={'pk': 6969}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewStudentTest(TestCase):
    """ Test case for create new record of Student """

    def setUp(self):
        self.valid_payload = {
          'first_name': 'string',
          'last_name': 'string',
          'surname': 'string',
          'grade': 2,
          'date_of_birth': '2021-01-21'
        }
        self.valid_payload2 = {
          'first_name': 'string2',
          'last_name': 'string3',
          'grade': 5,
          'date_of_birth': '1989-01-21'
        }
        self.invalid_payload = {
          'first_name': 'string',
          'last_name': 'string',
          'surname': 'string',
          'grade': 9,
          'date_of_birth': '2021-01-21'
        }
        self.invalid_payload2 = {
          'first_name22222': 'string',
          'last_name': 'string',
          'surname': 'string',
          'grade': 3,
          'date_of_birth': '2021-01-21'
        }

    def test_create_valid_students(self):
        for payload in [self.valid_payload, self.valid_payload2]:
            response = client.post(
                reverse('list_endpoint'),
                data=json.dumps(payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_experiment(self):
        for payload in [self.invalid_payload, self.invalid_payload2]:
            response = client.post(
                reverse('list_endpoint'),
                data=json.dumps(payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateStudentTest(TestCase):
    """ Test case for update record of Student """

    def setUp(self):
        self.student = Student.objects.create(
            first_name='first_name2',
            surname='surname2',
            last_name='last_name2',
            date_of_birth=datetime.date(month=2, year=1992, day=2),
            grade=2
        )
        self.valid_payload = {
          'first_name': 'fn1',
          'last_name': 'ln2',
          'surname': 'sn2',
          'grade': 5,
          'date_of_birth': '1999-01-21'
        }
        self.invalid_payload = {
          'first_name': 'fn1',
          'last_name': 'ln2',
          'surname': 'sn2',
          'grade': 9,
          'date_of_birth': '1999-01-21'
        }

    def test_valid_update_student(self):
        response = client.put(
            reverse('records_endpoint', kwargs={'pk': self.student.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_student(self):
        response = client.put(
            reverse('records_endpoint', kwargs={'pk': self.student.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteStudentTest(TestCase):
    """ Test module for deleting an existing experiment record """

    def setUp(self):
        self.student = Student.objects.create(
            first_name='first_name4',
            surname='surname4',
            last_name='last_name4',
            date_of_birth=datetime.date(month=4, year=1994, day=4),
            grade=4
        )

    def test_valid_delete_student(self):
        response = client.delete(
            reverse('records_endpoint', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_student(self):
        response = client.delete(
            reverse('records_endpoint', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
