# Generated by Django 4.2.3 on 2023-08-19 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgAdmin', '0004_semester_alter_announcement_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='time',
            field=models.TimeField(default=datetime.time(17, 30, 47, 481434)),
        ),
    ]
