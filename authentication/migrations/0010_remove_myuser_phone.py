# Generated by Django 3.0.8 on 2020-07-18 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20200718_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='phone',
        ),
    ]
