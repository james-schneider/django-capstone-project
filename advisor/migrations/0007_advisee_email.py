# Generated by Django 2.1.5 on 2019-03-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0006_auto_20190224_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisee',
            name='email',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]