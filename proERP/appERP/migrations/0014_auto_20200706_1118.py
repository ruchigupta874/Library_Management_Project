# Generated by Django 3.0.3 on 2020-07-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appERP', '0013_auto_20200706_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_login',
            name='l_password',
            field=models.CharField(default='ncuindia', max_length=200),
        ),
    ]