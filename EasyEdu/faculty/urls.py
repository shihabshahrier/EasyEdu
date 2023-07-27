from django.urls import path
from . import views

urlpatterns = [
    path('faculty-home/', views.facultyHome, name='faculty-home'),
]