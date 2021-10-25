from django.db import models
from django.contrib.auth.models import User
from .parametros import CHOICES
from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    universidad = models.IntegerField( 
        max_length = 100, 
        choices = CHOICES, 
        default = 1
        ) 
    
    def __str__(self):
        return self.user.first_name

class Course(models.Model):
    name = models.CharField(max_length=50)
    semester = models.IntegerField()
    year = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    promedio = models.FloatField(default=0)

    def __str__(self):
        return self.name
        

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    score = models.FloatField(default=0.0)
    ponderacion = models.FloatField(default=0.0)

    def ponderacion_perc(self):
        return int(self.ponderacion*100)

    def __str__(self):
        return self.name


