from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.announcements, name='announcements'),
    path('student/', views.student, name='student')
]