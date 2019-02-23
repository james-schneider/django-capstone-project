# Generated by Django 2.1.5 on 2019-02-23 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0002_corecoursegrade_electivecoursegrade_minorcoursegrade_secondmajorcoursegrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corecoursegrade',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisor.CoreCourse'),
        ),
        migrations.AlterField(
            model_name='electivecoursegrade',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisor.ElectiveCourse'),
        ),
        migrations.AlterField(
            model_name='minorcoursegrade',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisor.MinorCourse'),
        ),
        migrations.AlterField(
            model_name='secondmajorcoursegrade',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisor.SecondMajorCourse'),
        ),
    ]
