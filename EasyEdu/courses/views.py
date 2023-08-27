from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import STUDENT, FACULTY, ORG
from advising.models import PreAdvising, StudentAdvising
from courses.models import (
    Course,
    CourseSections,
    WeeklyMaterials,
    Quiz,
    FacultyCourseMapping,
)
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url="login")
def studentCourses(request):
    student = STUDENT.objects.get(user=request.user)
    if student:
        advising = StudentAdvising.objects.get(student=student)
        courses = advising.courses.all()
        sections = advising.section.all()
        sections_ = []
        print(sections)
        for section in sections:
            if section.section_end_time > datetime.now().time():
                sections_.append(section)

        return render(
            request,
            "courses/student_courses.html",
            {"courses": courses, "sections": sections_},
        )


@login_required(login_url="login")
def archiveCourses(request):
    student = STUDENT.objects.get(user=request.user)
    if student:
        advising = StudentAdvising.objects.get(student=student)
        courses = advising.courses.all()
        sections = advising.section.all()
        sections_ = []
        for section in sections:
            if section.section_end_time < datetime.now().time():
                sections_.append(section)

        return render(
            request,
            "courses/archived_course.html",
            {"courses": courses, "sections": sections_},
        )
    # return render(request, "courses/archived_course.html")


@login_required(login_url="login")
def facultyCourses(request):
    faculty = FACULTY.objects.get(user=request.user)
    if faculty:
        sections = CourseSections.objects.filter(faculty=faculty)

    return render(
        request,
        "courses/faculty_courses.html",
        {"sections": sections},
    )


@login_required(login_url="login")
def courseSecMap(request, section_id):
    section = CourseSections.objects.get(section_id=section_id)
    course = Course.objects.get(course_id=section.course.course_id)
    faculty = FACULTY.objects.get(user=request.user)
    weeks = WeeklyMaterials.objects.filter(section=section)

    if FACULTY.objects.get(user=request.user):
        user_type = "faculty"
    else:
        user_type = "student"

    if request.method == "POST":
        form = request.POST.get("form")
        if form == "f2":
            week_no = request.POST.get("week_no")
            week_title = request.POST.get("week_title")
            videos_link = request.POST.get("video_link")
            slides_link = request.POST.get("slide_link")

            embaded_link = videos_link.replace("watch?v=", "embed/")
            print(embaded_link)
            wkm = WeeklyMaterials.objects.create(
                week=section.section_id + "_" + week_no,
                title=week_title,
                week_no=week_no,
                faculty=faculty,
                course=course,
                section=section,
                videos_link=embaded_link,
                slides_link=slides_link,
            )
            wkm.save()

            return redirect("courseSecMap", section_id=section_id)
            print(week_no, week_title, videos_link, slides_link)
    print(section_id, "************")
    return render(
        request, "courses/course_map.html", {"weeks": weeks, "user_type": user_type}
    )


@login_required(login_url="login")
def studentCourseSecMap(request, section_id):
    section = CourseSections.objects.get(section_id=section_id)
    course = Course.objects.get(course_id=section.course.course_id)
    student = STUDENT.objects.get(user=request.user)
    weeks = WeeklyMaterials.objects.filter(section=section)
    print(weeks)

    print(section_id, "************")
    return render(
        request,
        "courses/student_course_map.html",
        {
            "weeks": weeks,
        },
    )


@login_required(login_url="login")
def weeklyMaterial(request, section_id, week):
    section = CourseSections.objects.get(section_id=section_id)
    course = Course.objects.get(course_id=section.course.course_id)
    faculty = FACULTY.objects.get(user=request.user)
    wkm = WeeklyMaterials.objects.filter(section=section)

    return render(request, "courses/weekly_materials.html", {"wkm": wkm[0]})


@login_required(login_url="login")
def studentWeeklyMaterial(request, section_id, week):
    section = CourseSections.objects.get(section_id=section_id)
    course = Course.objects.get(course_id=section.course.course_id)
    student = STUDENT.objects.get(user=request.user)
    wkm = WeeklyMaterials.objects.filter(section=section)

    return render(
        request, "courses/student_weekly_materials.html", {"wkm": wkm[0] if wkm else []}
    )
