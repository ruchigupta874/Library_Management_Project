# Generated by Django 3.0.3 on 2020-07-06 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appERP', '0010_auto_20200704_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminlogin',
            name='name',
            field=models.CharField(default='ruchi', max_length=200),
        ),
    ]
