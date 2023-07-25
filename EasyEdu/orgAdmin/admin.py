from django.contrib import admin
from .models import Announcement, EnrolledStudents

# Register your models here.
admin.site.register(Announcement)
admin.site.register(EnrolledStudents)
