# Generated by Django 4.2.3 on 2023-08-12 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('advising', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentadvising',
            name='courses',
            field=models.ManyToManyField(to='courses.course'),
        ),
        migrations.AddField(
            model_name='studentadvising',
            name='section',
            field=models.ManyToManyField(to='courses.coursesections'),
        ),
        migrations.AddField(
            model_name='studentadvising',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AddField(
            model_name='preadvising',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
    ]
