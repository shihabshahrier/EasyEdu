from django.db import models
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()


# Create your models here.
class ADMIN(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_name = models.CharField(max_length=100)
    admin_email = models.EmailField(max_length=100)
    admin_phone = models.CharField(max_length=10)
    admin_address = models.CharField(max_length=100)
    admin_photo = models.ImageField(upload_to='admin_photo/', blank=True)
    def __str__(self):
        return self.admin_name
    
class ORG(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=100)
    org_email = models.EmailField(max_length=100)
    org_phone = models.CharField(max_length=10)
    org_address = models.CharField(max_length=100)
    customer_type = models.CharField(max_length=100)
    org_logo = models.ImageField(upload_to='org_logo/', blank=True)


    def __str__(self):
        return self.org_name
    
class FACULTY(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org = models.ForeignKey(ORG, on_delete=models.CASCADE)
    faculty_name = models.CharField(max_length=100)
    faculty_email = models.EmailField(max_length=100)
    faculty_phone = models.CharField(max_length=10)
    faculty_address = models.CharField(max_length=100)
    faculty_photo = models.ImageField(upload_to='faculty_photo/', blank=True)
    department = models.CharField(max_length=100)
    session = models.CharField(max_length=100, default='None')
    joinin_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.faculty_name
    
class STUDENT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org = models.ForeignKey(ORG, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100, default='None')
    student_email = models.EmailField(max_length=100, default='None')
    student_phone = models.CharField(max_length=10, default='None')
    student_address = models.CharField(max_length=100, default='None')
    student_photo = models.ImageField(upload_to='student_photo/', blank=True)
    department = models.CharField(max_length=100, default='None')
    credit = models.IntegerField(default=0)
    session = models.CharField(max_length=100, default='None')
    joinin_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.student_name
    
    
