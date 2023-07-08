# Generated by Django 4.2.3 on 2023-07-08 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TEACHER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=100)),
                ('teacher_email', models.EmailField(max_length=100)),
                ('teacher_phone', models.CharField(max_length=10)),
                ('teacher_address', models.CharField(max_length=100)),
                ('teacher_photo', models.ImageField(blank=True, upload_to='teacher_photo/')),
                ('deperment', models.CharField(default='None', max_length=100)),
                ('joinin_date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='STUDENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=100)),
                ('student_phone', models.CharField(max_length=10)),
                ('student_address', models.CharField(max_length=100)),
                ('student_photo', models.ImageField(blank=True, upload_to='student_photo/')),
                ('deperment', models.CharField(max_length=100)),
                ('joinin_date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ORG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=100)),
                ('org_email', models.EmailField(max_length=100)),
                ('org_phone', models.CharField(max_length=10)),
                ('org_address', models.CharField(max_length=100)),
                ('org_logo', models.ImageField(blank=True, upload_to='org_logo/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ADMIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=100)),
                ('admin_email', models.EmailField(max_length=100)),
                ('admin_phone', models.CharField(max_length=10)),
                ('admin_address', models.CharField(max_length=100)),
                ('admin_photo', models.ImageField(blank=True, upload_to='admin_photo/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
