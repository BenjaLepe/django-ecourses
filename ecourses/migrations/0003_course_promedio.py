# Generated by Django 3.0.8 on 2020-08-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecourses', '0002_exam_ponderacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='promedio',
            field=models.FloatField(default=0),
        ),
    ]