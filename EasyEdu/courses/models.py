from django.db import models
from users.models import STUDENT, FACULTY, ORG

# Create your models here.


class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    org = models.ForeignKey(ORG, on_delete=models.CASCADE)
    course_title = models.CharField(max_length=100)
    course_credit = models.IntegerField(default=0)
    course_description = models.TextField()
    course_prerequisite = models.CharField(max_length=100)
    # course_type = models.CharField(max_length=100)
    # course_category = models.CharField(max_length=100)
    course_department = models.CharField(max_length=100)

    def __str__(self):
        return self.course_id


class CourseSections(models.Model):
    section_id = models.CharField(max_length=10, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(FACULTY, on_delete=models.CASCADE)
    section_capacity = models.IntegerField(default=0)
    section_enrolled = models.IntegerField(default=0)
    section_day = models.CharField(max_length=10)
    section_start_time = models.TimeField()
    section_end_time = models.TimeField()
    section_room = models.CharField(max_length=10)
    section_session = models.CharField(max_length=10)
    # section_semester = models.CharField(max_length=10)

    def __str__(self):
        return self.section_id


class WeeklyMaterials(models.Model):
    week = models.CharField(max_length=20, primary_key=True)
    week_no = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    faculty = models.ForeignKey(FACULTY, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(CourseSections, on_delete=models.CASCADE)
    videos_link = models.CharField(max_length=1000)
    slides_link = models.CharField(max_length=1000)

    def __str__(self):
        return (
            self.faculty.user.username
            + " - "
            + self.course.course_id
            + " - "
            + self.section.section_id
            + " - "
            + str(self.week)
        )


class Quiz(models.Model):
    quiz = models.CharField(max_length=20, primary_key=True)
    faculty = models.ForeignKey(FACULTY, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(CourseSections, on_delete=models.CASCADE)
    quiz_no = models.IntegerField(default=0)
    quiz_link = models.CharField(max_length=100)

    def __str__(self):
        return (
            self.faculty.user.username
            + " - "
            + self.course.course_id
            + " - "
            + self.section.section_id
            + " - "
            + str(self.quiz_no)
        )


class FacultyCourseMapping(models.Model):
    faculty = models.ForeignKey(FACULTY, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(CourseSections, on_delete=models.CASCADE)
    weeks = models.ForeignKey(WeeklyMaterials, on_delete=models.CASCADE)
    quizs = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return (
            self.faculty.user.username
            + " - "
            + self.course.course_id
            + " - "
            + self.section.section_id
        )
