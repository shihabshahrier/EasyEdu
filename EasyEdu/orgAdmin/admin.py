from django.contrib import admin
from .models import (
    Announcement,
    EnrolledStudents,
    RecruitedFaculty,
    PreAdvisingDetails,
    AdvisingDetails,
    Semester,
    otherInfo,
)

# Register your models here.
admin.site.register(Announcement)
admin.site.register(EnrolledStudents)
admin.site.register(RecruitedFaculty)
admin.site.register(PreAdvisingDetails)
admin.site.register(AdvisingDetails)
admin.site.register(Semester)
admin.site.register(otherInfo)
