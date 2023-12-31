# Generated by Django 4.2.3 on 2023-08-19 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgAdmin', '0007_alter_announcement_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='otherInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('session', models.CharField(max_length=100)),
                ('highest_credit', models.IntegerField()),
                ('lowest_credit', models.IntegerField()),
                ('price_per_credit', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='announcement',
            name='time',
            field=models.TimeField(default=datetime.time(20, 42, 22, 26231)),
        ),
    ]
