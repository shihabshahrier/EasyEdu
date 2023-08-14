from django.urls import path
from . import views

urlpatterns = [
    path('student-advising/', views.studentAdvising, name='advising'),
]