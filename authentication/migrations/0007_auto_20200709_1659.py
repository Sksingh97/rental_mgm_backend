# Generated by Django 3.0.8 on 2020-07-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20200709_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='country',
            field=models.CharField(max_length=255),
        ),
    ]
