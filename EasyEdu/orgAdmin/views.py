from django.shortcuts import render, redirect
from .models import Announcement, EnrolledStudents
from users.models import STUDENT, User
from users.models import ORG
import pandas as pd
import os


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
        file = request.FILES['file']
        session = request.POST['session']

        print("#==================== Test Start ================#")
        print(file)
        print(session)
        print("#==================== Test End ==================#")

        enrolledStudents = EnrolledStudents.objects.create(session=session, student_info_file=file)
        enrolledStudents.save()

        #adding students to the database
        df = pd.read_csv('media/student_info_files/'+str(file))

        for index, row in df.iterrows():
            if User.objects.filter(username=row['student_id']).exists():
                continue

            print(row['student_id'], row['first_name'], row['last_name'], row['email'], row['password'])
            user = User.objects.create(username=row['student_id'], email=row['email'], password= str(row['password']))
            user.save()
            student = STUDENT.objects.create(user = user, student_name=row['first_name']+" "+row['last_name'], student_email=row['email'])
            student.save()

        # deleting the file after adding the students to the database
        try:
            os.remove('media/student_info_files/'+str(file))
        except:
            print("File not found")
        return redirect('student')
    
    student = STUDENT.objects.all()
    return render(request, './orgAdmin/student.html', {'students': student})





