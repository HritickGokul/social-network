# Generated by Django 3.0.6 on 2020-05-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20200527_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
