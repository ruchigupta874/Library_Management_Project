# Generated by Django 3.0.7 on 2020-07-02 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appERP', '0007_auto_20200702_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_profile_pic',
        ),
    ]
