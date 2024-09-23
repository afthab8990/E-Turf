from django.db import models

class user(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.IntegerField()
    password=models.CharField(max_length=25)
    isverified=models.BooleanField(default=False)

class contact(models.Model):
    name=models.CharField(max_length=50)
    message=models.CharField(max_length=250)


    
# Create your models here.
