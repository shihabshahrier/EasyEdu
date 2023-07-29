# Generated by Django 4.2.3 on 2023-07-28 11:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0008_faculty_session_student_session_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreAdvising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adving_day', models.DateField(default=datetime.date.today)),
                ('adving_start_time', models.TimeField(default=datetime.time)),
                ('adving_end_time', models.TimeField(default=datetime.time)),
                ('session', models.CharField(default='Fall 2021', max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='Advising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adving_staring_day', models.DateField(default=datetime.date.today)),
                ('adving_ending_day', models.DateField(default=datetime.date.today)),
                ('adving_staring_time', models.TimeField(default=datetime.time)),
                ('adving_ending_time', models.TimeField(default=datetime.time)),
                ('session', models.CharField(default='Fall 2021', max_length=10)),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.faculty')),
                ('students', models.ManyToManyField(to='users.student')),
            ],
        ),
    ]