from django.urls import path
from . import views

urlpatterns = [
    path("student-home/", views.studentHome, name="student-home"),
    path("student-profile/", views.studentProfile, name="student-profile"),
    path("evaluation/", views.evaluation, name="evaluation"),
    path(
        "evaluation/<str:section_id>/", views.evaluateSection, name="evaluate-section"
    ),
    path("student-payment/", views.studentPayment, name="studentPayment"),
]
