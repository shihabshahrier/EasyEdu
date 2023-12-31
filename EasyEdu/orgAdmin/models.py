from django.db import models
from django.contrib.auth import get_user_model
import datetime
from users.models import ORG

User = get_user_model()
# Create your models here.


class Announcement(models.Model):
    announcement_id = models.AutoField(primary_key=True, unique=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(ORG, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.datetime.now().time())

    def __str__(self):
        return self.title + " " + str(self.date)


class EnrolledStudents(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    session = models.CharField(max_length=100)
    student_info_file = models.FileField(upload_to="student_info_files/")
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.id) + " " + self.session + " " + str(self.date)


class RecruitedFaculty(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    session = models.CharField(max_length=100)
    faculty_info_file = models.FileField(upload_to="faculty_info_files/")
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.id) + " " + self.session + " " + str(self.date)


class PreAdvisingDetails(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    session = models.CharField(max_length=100)
    pre_advising_file = models.FileField(upload_to="pre_advising_files/")
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.id) + " " + self.session + " " + str(self.date)


class AdvisingDetails(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    session = models.CharField(max_length=100)
    advising_file = models.FileField(upload_to="advising_files/")
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.id) + " " + self.session + " " + str(self.date)


class CourseDetails(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    session = models.CharField(max_length=100)
    course_file = models.FileField(upload_to="course_files/")
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.id) + " " + self.session + " " + str(self.date)


class Semester(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    session = models.CharField(max_length=100)
    semester_start_date = models.DateField(default=datetime.date.today)
    semester_end_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.id) + " " + self.session


class otherInfo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    session = models.CharField(max_length=100)
    highest_credit = models.IntegerField()
    lowest_credit = models.IntegerField()
    price_per_credit = models.IntegerField()

    def __str__(self):
        return str(self.id) + " " + self.session
