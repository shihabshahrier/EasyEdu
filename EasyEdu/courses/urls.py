from django.urls import path
from . import views

urlpatterns = [
    path("student-courses/", views.studentCourses, name="studentCourses"),
    path("faculty-courses/", views.facultyCourses, name="facultyCourses"),
    path("course-sec-map/<str:section_id>/", views.courseSecMap, name="courseSecMap"),
    path(
        "student-course-sec-map/<str:section_id>/",
        views.studentCourseSecMap,
        name="studentCourseSecMap",
    ),
    path(
        "course-sec-map/<str:section_id>/weeklyMaterial/<str:week>/",
        views.weeklyMaterial,
        name="weeklyMaterial",
    ),
    path(
        "student-course-sec-map/<str:section_id>/weeklyMaterial/<str:week>/",
        views.studentWeeklyMaterial,
        name="studentWeeklyMaterial",
    ),
    path("archived-courses/", views.archiveCourses, name="archiveCourses"),
]
