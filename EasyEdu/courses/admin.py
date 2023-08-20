from django.contrib import admin
from .models import (
    Course,
    CourseSections,
    WeeklyMaterials,
    Quiz,
    FacultyCourseMapping,
    Grade,
)

# Register your models here.

admin.site.register(Course)
admin.site.register(CourseSections)
admin.site.register(WeeklyMaterials)
admin.site.register(Quiz)
admin.site.register(FacultyCourseMapping)
admin.site.register(Grade)
