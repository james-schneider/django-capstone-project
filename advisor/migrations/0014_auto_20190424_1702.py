# Generated by Django 2.1.5 on 2019-04-24 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0013_auto_20190421_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='author',
        ),
        migrations.RemoveField(
            model_name='note',
            name='created_date',
        ),
    ]
