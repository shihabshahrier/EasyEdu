from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.announcements, name="announcements"),
    path("student/", views.student, name="student"),
    path("faculty/", views.faculty, name="faculty"),
    path("org-profile/", views.orgProfile, name="orgProfile"),
    path("control-panel/admin-pre-advising/", views.controlPanel, name="controlPanel"),
    path("control-panel/admin-courses/", views.adminCourse, name="adminCourses"),
    path("delete-faculty/<int:id>/", views.deleteFaculty, name="deleteFaculty"),
    path("delete-student/<int:id>/", views.deleteStudent, name="deleteStudent"),
]
