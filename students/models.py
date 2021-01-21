from django.db import models


class Student(models.Model):
    """Model for Student parameters"""

    BAD = 2
    POOR = 3
    GOOD = 4
    GREAT = 5

    MARKS = (
        (BAD, 'неуд'),
        (POOR, 'уд'),
        (GOOD, 'хор'),
        (GREAT, 'отл'),
    )

    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    surname = models.CharField('Отчество', max_length=255, null=True)
    grade = models.IntegerField('Успеваемость', choices=MARKS, default=BAD)
    date_of_birth = models.DateField('Дата рождения', auto_now=False,
                                     auto_now_add=False)
