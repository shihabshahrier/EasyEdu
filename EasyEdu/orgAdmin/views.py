from django.shortcuts import render, redirect
from .models import Announcement, EnrolledStudents, RecruitedFaculty
from users.models import STUDENT, User, FACULTY
from users.models import ORG
from django.contrib import messages
import pandas as pd
import os
import datetime
from django.db.models import Q


# Create your views here.
def announcements(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['text']
        org = ORG.objects.get(user=request.user)
        print("#==================== Test Start ================#")
        print(org)
        print("#==================== Test End ==================#")
        announcement = Announcement.objects.create(posted_by=request.user, body=body, title=title, org=org)
        announcement.save()
        return redirect('announcements')
    announcements = Announcement.objects.filter(org=ORG.objects.get(user=request.user))
    return render(request, './orgAdmin/home.html', {'announcements': announcements})


def student(request):
    if request.method == 'POST':
        form_no = request.POST['form']
        if form_no == 'f1':
            file = request.FILES['file']
            session = request.POST['session']

            print("#==================== Test Start ================#")
            print(file)
            print(session)
            print("#==================== Test End ==================#")

            # rename the file
            file.name = str(session)+".csv"

            enrolledStudents = EnrolledStudents.objects.create(session=session, student_info_file=file)
            enrolledStudents.save()

            #adding students to the database
            df = pd.read_csv('media/student_info_files/'+str(file))
            org = ORG.objects.get(user=request.user)
            for index, row in df.iterrows():
                if User.objects.filter(username=row['student_id']).exists():
                    continue

                print(row['student_id'], row['first_name'], row['last_name'], row['email'], row['password'], row['department'])
                user = User.objects.create(username=row['student_id'], email=row['email'])
                user.set_password(str(row['password']))
                print(row['password'])
                user.save()
                student = STUDENT.objects.create(user = user, org = org, student_name=row['first_name']+" "+row['last_name'], student_email=row['email'], department=row['department'], session=session)
                student.save()
                messages.info(request, 'Students added successfully')

            # deleting the file after adding the students to the database
            try:
                os.remove('media/student_info_files/'+str(file))
            except:
                print("File not found")
            return redirect('student')
        
        elif form_no == 'f2':
            print("Form 2")
            student_id = request.POST['student_id']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            department = request.POST['department']
            session = request.POST['session']

            full_name = first_name+" "+last_name

            if User.objects.filter(username=student_id).exists():
                messages.info(request, 'Student ID already exists')
                return redirect('student')
            else:
                user = User.objects.create(username=student_id, email=email)
                user.set_password(str(password))
                user.save()
                student = STUDENT.objects.create(user=user, org=ORG.objects.get(user=request.user), student_name=full_name, student_email=email, department=department, session=session)
                student.save()
                messages.info(request, 'Student added successfully')
                return redirect('student')
            
    elif request.method == 'GET':
        print("GET")
        query = request.GET.get("query")
        if query:
            # search with user id   
            student = STUDENT.objects.filter(Q(student_name__icontains=query) | Q(student_email__icontains=query) | Q(department__icontains=query) | Q(session__icontains=query) | Q(user__username__icontains=query))
            return render(request, './orgAdmin/student.html', {'students': student, 'cancel': True})

                
    student = STUDENT.objects.all()
    return render(request, './orgAdmin/student.html', {'students': student})

# same as student
def faculty(request):
    if request.method == 'POST':
        form_no = request.POST['form']
        if form_no == 'f1':
            session = request.POST['session']
            file = request.FILES['file']
            
            print("#==================== Test Start ================#")
            print(file)
            print("#==================== Test End ==================#")

            # rename the file
            file.name = str(session)+".csv"

            recruitedFaculty = RecruitedFaculty.objects.create(session=session, faculty_info_file=file)
            recruitedFaculty.save()

            #adding students to the database
            df = pd.read_csv('media/faculty_info_files/'+str(file))
            org = ORG.objects.get(user=request.user)
            for index, row in df.iterrows():
                if User.objects.filter(username=row['faculty_id']).exists():
                    continue

                print(row['faculty_id'], row['first_name'], row['last_name'], row['email'], row['password'], row['department'], row['joining_date'])
                user = User.objects.create(username=row['faculty_id'], email=row['email'])
                user.set_password(str(row['password']))
                print(row['password'])
                user.save()
                jdate = row['joining_date']
                joining_date = datetime.datetime.strptime(jdate, '%Y-%m-%d').date()

                faculty = FACULTY.objects.create(user = user, org = org, faculty_name=row['first_name']+" "+row['last_name'], faculty_email=row['email'], department=row['department'], joinin_date= jdate, session=session)
                messages.info(request, 'Faculty added successfully')
                faculty.save()
            
            

            # deleting the file after adding the students to the database
            try:
                os.remove('media/faculty_info_files/'+str(file))
            except:
                print("File not found")
            return redirect('faculty')
        
        elif form_no == 'f2':
            print("Form 2")
            faculty_id = request.POST['faculty_id']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            department = request.POST['department']
            joining_date = request.POST['joining_date']
            session = request.POST['session']

            full_name = first_name+" "+last_name

            if User.objects.filter(username=faculty_id).exists():
                messages.info(request, 'Faculty ID already exists')
                return redirect('faculty')
            else:
                user = User.objects.create(username=faculty_id, email=email)
                user.set_password(str(password))
                user.save()
                faculty = FACULTY.objects.create(user=user, org=ORG.objects.get(user=request.user), faculty_name=full_name, faculty_email=email, department=department, joinin_date=joining_date, session=session)
                faculty.save()
                messages.info(request, 'Faculty added successfully')
                return redirect('faculty')
    elif request.method == 'GET':
        print("GET")
        query = request.GET.get("query")
        if query:
            # search with user id   
            faculty = FACULTY.objects.filter(Q(faculty_name__icontains=query) | Q(faculty_email__icontains=query) | Q(department__icontains=query) | Q(session__icontains=query) | Q(user__username__icontains=query))
            return render(request, './orgAdmin/faculty.html', {'faculty': faculty, 'cancel': True})
            
    faculty = FACULTY.objects.all()
    return render(request, './orgAdmin/faculty.html', {'faculty': faculty, 'cancel': False})
