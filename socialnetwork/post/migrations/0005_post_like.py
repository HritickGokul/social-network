# Generated by Django 3.0.6 on 2020-05-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200525_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
