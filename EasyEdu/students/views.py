from django.shortcuts import render
from users.models import STUDENT, FACULTY, ORG, User
from orgAdmin.models import Announcement
from advising.models import PreAdvising, StudentAdvising
from courses.models import Course, CourseSections


# Create your views here.
def studentHome(request):
    student = STUDENT.objects.get(user=request.user)
    org = student.org
    announcements = Announcement.objects.filter(org=org)

    return render(
        request, "./student/student_home.html", {"announcements": announcements}
    )


def studentProfile(request):
    student = STUDENT.objects.get(user=request.user)
    return render(request, "./student/profile.html", {"student": student})


def evaluation(request):
    student = STUDENT.objects.get(user=request.user)
    student_advising = StudentAdvising.objects.get(student=student)
    courses = student_advising.courses.all()

    return render(request, "./student/evaluation.html", {"courses": courses})
