from django.contrib import admin
from .models import Announcement, EnrolledStudents, RecruitedFaculty

# Register your models here.
admin.site.register(Announcement)
admin.site.register(EnrolledStudents)
admin.site.register(RecruitedFaculty)

