import datetime

from django.test import TestCase
from ..models import Student


class StudentTest(TestCase):
    """ Test cases for Django Student model """
    TEST_GRADE_VALUE = 2
    TEST_SURNAME_VALUE = 'Testovitch'
    TEST_LAST_NAME_VALUE = 'Testov'
    TEST_FIRST_NAME_VALUE = 'Testo'
    TEST_BIRTH_DATE = datetime.date(month=1, year=1994, day=3)

    def setUp(self):
        """ Prepare test instance of Student """
        Student.objects.create(
            first_name=self.TEST_FIRST_NAME_VALUE,
            surname=self.TEST_SURNAME_VALUE,
            last_name=self.TEST_LAST_NAME_VALUE,
            date_of_birth=self.TEST_BIRTH_DATE,
            grade=self.TEST_GRADE_VALUE
        )

    def test_student_attributes(self):
        """ Check validity of Student's attributes """
        test_student = Student.objects.filter().latest('id')
        self.assertEqual(test_student.grade, self.TEST_GRADE_VALUE)
        self.assertEqual(test_student.date_of_birth, self.TEST_BIRTH_DATE)
        self.assertEqual(test_student.last_name, self.TEST_LAST_NAME_VALUE)
        self.assertEqual(test_student.surname, self.TEST_SURNAME_VALUE)
        self.assertEqual(test_student.first_name, self.TEST_FIRST_NAME_VALUE)
