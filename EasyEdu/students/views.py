from django.shortcuts import render, redirect
import stripe
from users.models import STUDENT, FACULTY, ORG, User
from orgAdmin.models import Announcement, Semester, otherInfo
from advising.models import PreAdvising, StudentAdvising
from courses.models import Course, CourseSections, Grade, WeeklyMaterials, Quiz
from .models import Payment, Evaluation
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
@login_required(login_url='login')
def studentHome(request):
    student = STUDENT.objects.get(user=request.user)
    org = student.org
    announcements = Announcement.objects.filter(org=org)

    return render(
        request, "./student/student_home.html", {"announcements": announcements}
    )

@login_required(login_url='login')
def studentProfile(request):
    student = STUDENT.objects.get(user=request.user)
    if request.method == "POST":
        print("##########", "post")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        profile_pic = request.FILES.get("profile_pic")

        student.user.name = name
        student.user.email = email
        student.user.phone = phone
        student.user.address = address

        student.student_name = name
        student.student_email = email
        student.student_phone = phone
        student.student_address = address

        if profile_pic:
            student.student_photo = profile_pic
        student.user.save()
        student.save()

        return redirect("student-profile")
    return render(request, "./student/profile.html", {"user": student})

@login_required(login_url='login')
def evaluation(request):
    student = STUDENT.objects.get(user=request.user)
    student_advising = StudentAdvising.objects.get(student=student)
    courses = student_advising.section.all()
    for c in courses:
        if c.evaluation_set.filter(student=student).exists():
            courses = courses.exclude(section_id=c.section_id)

    return render(request, "./student/evaluate.html", {"courses": courses})

@login_required(login_url='login')
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

@login_required(login_url='login')
def studentPayment(request):
    student = STUDENT.objects.get(user=request.user)
    current_semester = Semester.objects.all().last()
    payment = Payment.objects.filter(student=student, semester=current_semester)
    # print(payment)
    if not payment.exists():
        courses = StudentAdvising.objects.get(student=student).section.all()
        other = otherInfo.objects.all().last()
        total_course_fee = []
        for course in courses:
            total_course_fee.append(
                course.course.course_credit * other.price_per_credit
            )
        print(total_course_fee)

        lst = zip(courses, total_course_fee)
        return render(
            request,
            "./student/payment.html",
            {
                "courses": courses,
                "pkey": settings.STRIPE_PUBLISHABLE_KEY,
                "total": sum(total_course_fee),
                "lst": lst,
                "payment": False,
            },
        )
    else:
        return render(request, "./student/payment.html", {"payment": True})

@login_required(login_url='login')
def ypay(request):
    student = STUDENT.objects.get(user=request.user)
    courses = StudentAdvising.objects.get(student=student).section.all()
    other = otherInfo.objects.all().last()
    total_course_fee = 0
    for course in courses:
        total_course_fee += course.course.course_credit * other.price_per_credit
    if request.method == "POST":
        charge = stripe.Charge.create(
            amount=total_course_fee,
            currency="usd",
            description="Course Payment",
            source=request.POST["stripeToken"],
        )
        student = STUDENT.objects.get(user=request.user)
        semester = Semester.objects.all().last()
        payment = Payment.objects.create(
            student=student, semester=semester, amount=total_course_fee, status=True
        )
        payment.save()

        return render(request, "./student/ypay.html")

@login_required(login_url='login')
def grades(request):
    student = STUDENT.objects.get(user=request.user)
    student_advising = StudentAdvising.objects.get(student=student)
    courses = student_advising.section.all()
    semester = Semester.objects.all().last()

    graded = Grade.objects.filter(student=student)
    print(graded)

    return render(
        request, "./student/grade_sheet.html", {"semester": semester, "graded": graded}
    )
