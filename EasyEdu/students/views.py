from django.shortcuts import render, redirect
from users.models import STUDENT, FACULTY, ORG, User
from orgAdmin.models import Announcement
from advising.models import PreAdvising, StudentAdvising
from courses.models import Course, CourseSections
from .models import Payment, Evaluation
from datetime import datetime


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
    courses = student_advising.section.all()
    for c in courses:
        if c.evaluation_set.filter(student=student).exists():
            courses = courses.exclude(section_id=c.section_id)

    return render(request, "./student/evaluate.html", {"courses": courses})


def evaluateSection(request, section_id):
    student = STUDENT.objects.get(user=request.user)
    student_advising = StudentAdvising.objects.get(student=student)
    if request.method == "POST":
        print("##########")
        rating = request.POST.get("rating")
        feedback = request.POST.get("feedback")
        section = CourseSections.objects.get(section_id=section_id)
        course = section.course
        faculty = section.faculty
        print(rating, feedback, section, course, faculty)
        evaluation = Evaluation.objects.create(
            student=student,
            section=section,
            course=course,
            faculty=faculty,
            rating=int(rating),
            comment=feedback,
            date=datetime.now(),
        )
        evaluation.save()

        return redirect("evaluation")
    return render(request, "./student/evaluation.html", {"section_id": section_id})


def studentPayment(request):
    return render(request, "./student/payment.html")
