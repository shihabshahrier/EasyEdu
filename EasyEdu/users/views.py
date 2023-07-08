from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ADMIN, ORG, TEACHER, STUDENT

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
    return render(request, './auth/login.html')
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        password2 = request.POST['confirmpass']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                org = ORG.objects.create(user=user, org_name=username, org_email=email)
                org.save()
                return redirect('login')
        else:
            return render(request, './auth/reg.html')

    return render(request, './auth/reg.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def home(request):
    return render(request, './home/index.html')


