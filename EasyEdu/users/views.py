from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ADMIN, ORG, STUDENT, FACULTY
from orgAdmin.views import announcements
from students.views import studentHome
from faculty.views import facultyHome


# Create your views here.
def login(request):
    if request.method == "POST":
        user_type = request.POST["user_type"]
        username = request.POST["username"]
        password = request.POST["pass"]

        print(user_type, username, password)

        if user_type == "p1":
            user = authenticate(username=username, password=password)
            if user is not None and ORG.objects.filter(user=user).exists():
                auth.login(request, user)
                return redirect("announcements")
            else:
                messages.info(request, "Invalid Credentials")
                return redirect("login")
        elif user_type == "p2":
            user = authenticate(username=username, password=password)
            if user is not None and FACULTY.objects.filter(user=user).exists():
                auth.login(request, user)
                return redirect(facultyHome)
            else:
                messages.info(request, "Invalid Credentials")
                return redirect("login")
        elif user_type == "p3":
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None and STUDENT.objects.filter(user=user).exists():
                auth.login(request, user)
                return redirect(studentHome)
    return render(request, "./auth/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["pass"]
        password2 = request.POST["confirmpass"]

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()

                org = ORG.objects.create(user=user, org_name=username, org_email=email)
                org.save()
                return redirect("login")
        else:
            return render(request, "./auth/reg.html")

    return render(request, "./auth/reg.html")


def logout(request):
    auth.logout(request)
    return redirect("login")
