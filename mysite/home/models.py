from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField()
    # image = models.ImageField(upload_to="images")
    # file = models.FileField()

class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)
