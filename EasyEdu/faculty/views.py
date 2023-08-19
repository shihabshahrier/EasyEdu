from django.shortcuts import render
from users.models import STUDENT, FACULTY, ORG
from orgAdmin.models import Announcement


# Create your views here.
def facultyHome(request):
    faculty = FACULTY.objects.get(user=request.user)
    announcements = Announcement.objects.filter(org=faculty.org)
    return render(
        request, "./faculty/faculty_home.html", {"announcements": announcements}
    )


def facultyProfile(request):
    faculty = FACULTY.objects.get(user=request.user)
    return render(request, "./faculty/profile.html", {"faculty": faculty})
