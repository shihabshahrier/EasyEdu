# Generated by Django 4.2.3 on 2023-07-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_org_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='user_type',
            field=models.CharField(max_length=100),
        ),
    ]
