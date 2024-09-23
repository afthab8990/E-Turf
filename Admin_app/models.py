from django.db import models
from Manager_app.models import *
from User_app.models import *

class location(models.Model):
    city=models.CharField(max_length=25)
    cityimage=models.ImageField()

class turf(models.Model):
    turfname=models.CharField(max_length=40)
    capacity=models.IntegerField()
    rate=models.IntegerField()
    turfimage=models.ImageField() 
    turflocation=models.CharField(max_length=25)
    isbooked=models.BooleanField(default=False)
    managerof=models.CharField(max_length=100)
    # hasslots=models.BooleanField(default=False)

class booking(models.Model):
    buser=models.ForeignKey(user,on_delete=models.CASCADE)
    bturf=models.ForeignKey(turf,on_delete=models.CASCADE)
    bslot=models.CharField(max_length=100)
    booked=models.TextField(default='not booked yet')

# Create your models here.
