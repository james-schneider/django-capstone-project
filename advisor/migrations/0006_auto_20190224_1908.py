# Generated by Django 2.1.5 on 2019-02-25 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0005_auto_20190224_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisee',
            name='first_major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advisee_first_major', to='advisor.StudyMajor'),
        ),
        migrations.AlterField(
            model_name='advisee',
            name='second_major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advisee_second_major', to='advisor.StudyMajor'),
        ),
    ]
