from django.urls import path
from . import views

urlpatterns = [
    path('student-home/', views.studentHome, name='student-home'),
]