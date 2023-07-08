from django.db import models
from django.contrib.auth import get_user_model

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
    org_logo = models.ImageField(upload_to='org_logo/', blank=True)

    def __str__(self):
        return self.org_name
    
class TEACHER(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=100)
    teacher_email = models.EmailField(max_length=100)
    teacher_phone = models.CharField(max_length=10)
    teacher_address = models.CharField(max_length=100)
    teacher_photo = models.ImageField(upload_to='teacher_photo/', blank=True)
    deperment = models.CharField(max_length=100, default='None')
    joinin_date = models.DateField()

    def __str__(self):
        return self.teacher_name
    
class STUDENT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    student_phone = models.CharField(max_length=10)
    student_address = models.CharField(max_length=100)
    student_photo = models.ImageField(upload_to='student_photo/', blank=True)
    deperment = models.CharField(max_length=100)
    joinin_date = models.DateField()


    def __str__(self):
        return self.student_name
    
    
