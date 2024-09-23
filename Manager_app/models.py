from django.db import models

class manager(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.IntegerField()
    password=models.CharField(max_length=25)
    isassigned=models.IntegerField(default=0)
    isapproved=models.BooleanField(default=False)
# Create your models here.
