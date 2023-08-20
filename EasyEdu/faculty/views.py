from django.shortcuts import render, redirect
from users.models import STUDENT, FACULTY, ORG
from orgAdmin.models import Announcement, Semester
from courses.models import Course, CourseSections, Grade, WeeklyMaterials, Quiz
import pandas as pd
from django.contrib.auth.models import User


# Create your views here.
def facultyHome(request):
    faculty = FACULTY.objects.get(user=request.user)
    announcements = Announcement.objects.filter(org=faculty.org)
    return render(
        request, "./faculty/faculty_home.html", {"announcements": announcements}
    )


def facultyProfile(request):
    faculty = FACULTY.objects.get(user=request.user)
    if request.method == "POST":
        print("##########", "post")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        profile_pic = request.FILES.get("profile_pic")

        faculty.user.name = name
        faculty.user.email = email
        faculty.user.phone = phone
        faculty.user.address = address
        faculty.user.save()
        print("##########", profile_pic)
        faculty.faculty_name = name
        faculty.faculty_email = email
        faculty.faculty_phone = phone
        faculty.faculty_address = address
        if profile_pic:
            faculty.faculty_photo = profile_pic
        faculty.save()

        return redirect("faculty-profile")
    return render(request, "./faculty/profile.html", {"user": faculty})


def submitGradeSection(request):
    faculty = FACULTY.objects.get(user=request.user)
    sections = CourseSections.objects.filter(faculty=faculty)
    return render(request, "./faculty/submit_grade_sec.html", {"sections": sections})


def submitGrade(request, section_id):
    faculty = FACULTY.objects.get(user=request.user)
    # sections = CourseSections.objects.filter(faculty=faculty)
    section = CourseSections.objects.get(section_id=section_id)
    course = section.course
    current_semester = Semester.objects.all().last()
    print("##########", section_id)
    if request.method == "POST":
        file = request.FILES.get("file")

        file.name = f"{section_id}{current_semester}.csv"
        df = pd.read_csv(file)
        print(df)

        for index, row in df.iterrows():
            student = row["Student"]
            grade = row["Grade"]

            user = User.objects.get(username=student)
            student = STUDENT.objects.get(user=user)

            grade = Grade.objects.create(
                grade_id=f"{section_id}{student.user.username}{current_semester}",
                student=student,
                course=course,
                section=section,
                grade=grade,
                session=current_semester.session,
            )
            grade.save()
            print(grade)

        return redirect("submit-grade-section")

    return render(request, "./faculty/submit_grade.html", {"section_id": section_id})
