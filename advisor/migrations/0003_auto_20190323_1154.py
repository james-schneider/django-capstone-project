# Generated by Django 2.1.5 on 2019-03-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0002_majorcourse_is_developmental'),
    ]

    operations = [
        migrations.AddField(
            model_name='corecourse',
            name='is_developmental',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='electivecourse',
            name='is_developmental',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='secondmajorcourse',
            name='is_developmental',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
