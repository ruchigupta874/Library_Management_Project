# Generated by Django 3.0.3 on 2020-07-09 05:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appERP', '0017_auto_20200709_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 19, 5, 52, 15, 332817, tzinfo=utc)),
        ),
    ]
