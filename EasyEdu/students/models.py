from django.db import models
from django.contrib.auth.models import User
from users.models import STUDENT
from orgAdmin.models import Semester


# Create your models here.
class Payment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.student.username
