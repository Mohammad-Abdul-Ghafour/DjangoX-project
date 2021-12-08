from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import manager

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15 , null=True,blank=True)
    # email = models.EmailField(null=True,blank=True)
    roll = models.CharField(max_length=10,null=False,blank=False,choices=[('owner','owner'),('manager','manger')],default='owner')

    def __str__(self):
        return self.username