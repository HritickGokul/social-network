# Generated by Django 3.0.6 on 2020-05-17 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200517_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='user',
            name='width_field',
        ),
    ]
