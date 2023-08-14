from django.db import models
from django.contrib.auth.models import User
from users.models import STUDENT, FACULTY, ORG
from courses.models import Course, CourseSections
import datetime


# Create your models here.
class PreAdvising(models.Model):
    student = models.ForeignKey(STUDENT, on_delete=models.CASCADE)
    advising_day = models.DateField(default=datetime.date.today)
    advising_start_time = models.TimeField(default=datetime.time)
    advising_end_time = models.TimeField(default=datetime.time)
    session = models.CharField(max_length=10, default="Fall 2021")

    def __str__(self):
        return str(self.student) + str(self.advising_day)


class StudentAdvising(models.Model):
    advising_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(STUDENT, on_delete=models.CASCADE, unique=True)
    advisor = models.ForeignKey(FACULTY, on_delete=models.CASCADE, null=True)
    courses = models.ManyToManyField(Course)
    section = models.ManyToManyField(CourseSections)
    advising_day = models.DateField(default=datetime.date.today)
    advising_start_time = models.TimeField(default=datetime.time)
    advising_end_time = models.TimeField(default=datetime.time)
    session = models.CharField(max_length=10, default="Fall 2021")
    credit = models.IntegerField(default=0)

    def __str__(self):
        return str(self.student) + str(self.advisor) + str(self.advising_day)
