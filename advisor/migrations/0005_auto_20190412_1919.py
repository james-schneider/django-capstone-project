# Generated by Django 2.1.5 on 2019-04-12 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0004_futurecourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorcourse',
            name='credits',
            field=models.FloatField(default=3.0, max_length=10),
        ),
    ]
