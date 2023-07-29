from django.db import models
from django.contrib.auth.models import User
from users.models import STUDENT, FACULTY, ORG
import datetime

# Create your models here.
class PreAdvising(models.Model):
    student = models.ForeignKey(STUDENT, on_delete=models.CASCADE)
    advising_day = models.DateField(default=datetime.date.today)
    advising_start_time = models.TimeField(default=datetime.time)
    advising_end_time = models.TimeField(default=datetime.time)
    session = models.CharField(max_length=10, default='Fall 2021')

    def __str__(self):
        return str(self.student)+str(self.advising_day)
    
class Advising(models.Model):
    advisor = models.ForeignKey(FACULTY, on_delete=models.CASCADE)
    students = models.ManyToManyField(STUDENT)
    advising_staring_day = models.DateField(default=datetime.date.today)
    advising_ending_day = models.DateField(default=datetime.date.today)
    advising_staring_time = models.TimeField(default=datetime.time)
    advising_ending_time = models.TimeField(default=datetime.time)
    session = models.CharField(max_length=10, default='Fall 2021')

    def __str__(self):
        return str(self.advisor)+str(self.advising_staring_day)+str(self.advising_staring_time)
    

