# Generated by Django 2.1.5 on 2019-03-23 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='majorcourse',
            name='is_developmental',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]