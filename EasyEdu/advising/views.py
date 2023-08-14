from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import STUDENT, FACULTY, ORG
from .models import PreAdvising, StudentAdvising
from courses.models import Course, CourseSections
import datetime

# Create your views here.


def studentAdvising(request):
    user = User.objects.get(username=request.user.username)
    student = STUDENT.objects.get(user=user)
    print(student)
    today = datetime.date.today()
    time = datetime.datetime.now().time()
    pre_advising = PreAdvising.objects.filter(student=student, advising_day__gte=today)
    ispre_advising = False
    q_section = CourseSections.objects.all()
    advised = StudentAdvising.objects.filter(student=student)
    if (
        pre_advising
        and pre_advising[0].advising_start_time
        <= time
        <= pre_advising[0].advising_end_time
    ):
        ispre_advising = True

        if request.method == "GET":
            query = request.GET.get("query")
            if query:
                q_course = Course.objects.filter(course_id__icontains=query)
                q_section = CourseSections.objects.filter(course__in=q_course)

        if request.method == "POST":
            form_no = request.POST.get("form_no")
            if form_no == "f1":
                section_id = request.POST.get("section_id")
                sections = CourseSections.objects.get(section_id=section_id)
                course = Course.objects.get(course_id=sections.course_id)

                try:
                    advising = StudentAdvising.objects.get(student=student)
                except StudentAdvising.DoesNotExist:
                    advising = StudentAdvising.objects.create(
                        student=student,
                        advisor=None,
                        advising_day=pre_advising[0].advising_day,
                        advising_start_time=pre_advising[0].advising_start_time,
                        advising_end_time=pre_advising[0].advising_end_time,
                        session=pre_advising[0].session,
                    )
                    sections.section_capacity -= 1
                    sections.section_enrolled += 1
                    sections.save()
                    advising.save()

                if not advising.section.filter(course=course).exists():
                    advising.section.add(sections)
                    advising.courses.add(course)
                    advising.credit += course.course_credit
                    sections.section_enrolled += 1
                    sections.section_capacity -= 1
                    sections.save()
                    advising.save()

                return redirect("advising")

            elif form_no == "f2":
                section_id = request.POST.get("section_id")
                sections = CourseSections.objects.get(section_id=section_id)
                course = Course.objects.get(course_id=sections.course_id)

                advised_remove = StudentAdvising.objects.get(student=student)
                advised_remove.section.remove(sections)
                advised_remove.courses.remove(course)
                advised_remove.credit -= course.course_credit
                sections.section_enrolled -= 1
                sections.section_capacity += 1
                sections.save()
                advised_remove.save()

                return redirect("advising")

    return render(
        request,
        "advising/student_advising.html",
        {
            "ispre_advising": ispre_advising,
            "sections": q_section,
            "advised": advised[0].section.all() if advised else [],
        },
    )
