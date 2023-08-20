from django.db import models
from django.contrib.auth.models import User
from courses.models import Course, CourseSections

from users.models import STUDENT, FACULTY, ORG
from orgAdmin.models import Semester


# Create your models here.
class Payment(models.Model):
    student = models.ForeignKey(STUDENT, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.student.user.username


class Evaluation(models.Model):
    student = models.ForeignKey(STUDENT, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(CourseSections, on_delete=models.CASCADE)
    faculty = models.ForeignKey(FACULTY, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.username + " " + self.course + " " + self.section
