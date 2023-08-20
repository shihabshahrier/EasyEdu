from django.urls import path
from . import views

urlpatterns = [
    path("faculty-home/", views.facultyHome, name="faculty-home"),
    path("faculty-profile/", views.facultyProfile, name="faculty-profile"),
    path(
        "submit-grade-section/", views.submitGradeSection, name="submit-grade-section"
    ),
    path(
        "submit-grade-section/<str:section_id>/", views.submitGrade, name="submit-grade"
    ),
]
