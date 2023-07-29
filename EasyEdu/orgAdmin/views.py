from django.shortcuts import render, redirect
from .models import Announcement, EnrolledStudents, RecruitedFaculty, PreAdvisingDetails, AdvisingDetails
from users.models import STUDENT, User, FACULTY, ORG
from advising.models import PreAdvising, Advising
from django.contrib import messages
import pandas as pd
import os
import datetime
from datetime import datetime

from django.db.models import Q


#==================== admin home ====================#

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
    obj = ORG.objects.get(user=request.user)
    announcements = Announcement.objects.filter(org=ORG.objects.get(user=request.user))

    return render(request, './orgAdmin/home.html', {'announcements': announcements, "obj":obj})



#==================== admin student ====================#

def student(request):
    obj = ORG.objects.get(user=request.user)
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
            return render(request, './orgAdmin/student.html', {'students': student, 'cancel': True, "obj":obj})

                
    student = STUDENT.objects.all()
    return render(request, './orgAdmin/student.html', {'students': student, 'cancel': False, "obj":obj})


#==================== admin Faculty ====================#
# same as student
def faculty(request):
    obj = ORG.objects.get(user=request.user)
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
            return render(request, './orgAdmin/faculty.html', {'faculty': faculty, 'cancel': True, "obj":obj})
            
    faculty = FACULTY.objects.all()
    return render(request, './orgAdmin/faculty.html', {'faculty': faculty, 'cancel': False, "obj":obj})



#==================== admin profile ====================#

def orgProfile(request):
    obj = ORG.objects.get(user=request.user)
    return render(request, './orgAdmin/profile.html', {"obj":obj})




#==================== admin control panel ====================#

def controlPanel(request):
    if request.method == 'POST':
        file = request.FILES['file']
        session = request.POST['session']

        print("#==================== Test Start ================#")
        print(file)
        print(session)
        print("#==================== Test End ==================#")

        # rename the file
        file.name = str(session)+".csv"

        preAdvisingDetails = PreAdvisingDetails.objects.create(session=session, pre_advising_file=file)
        preAdvisingDetails.save()

        # adding pre advising details to the database
        df = pd.read_csv('media/pre_advising_files/'+str(file))

        student = STUDENT.objects.all()
        for s in student:
            for index, row in df.iterrows():
                l, h = map(int, row['Credit'].split('-'))
                start_time , end_time = map(str, row['Time Slot'].split('-'))
                s_time = datetime.strptime(start_time.strip(), '%I:%M%p').time()
                e_time = datetime.strptime(end_time.strip(), '%I:%M%p').time()
                ad_date = row['Date']
                print("###################")
                print(ad_date)
                advising_date = datetime.strptime(ad_date, '%m-%d-%Y').date()
                if l<=s.credit<=h:
                    pre_advising = PreAdvising.objects.create(student=s, adving_day=advising_date, adving_start_time= s_time, adving_end_time=e_time, session=session)
                    pre_advising.save()
                    break
        messages.info(request, 'Pre advising details added successfully')
        # deleting the file after adding the students to the database
        try:
            os.remove('media/pre_advising_files/'+str(file))
        except:
            print("File not found")
        return redirect('controlPanel')
    

    return render(request, './orgAdmin/controlPanel.html')