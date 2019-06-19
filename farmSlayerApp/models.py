from django.db import models

# Create your models here.
## users/modles.py

from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
  # add additional fields in here

  location = models.CharField(max_length=100, default='')
  phoneNumber = models.IntegerField(default=0)
  

  def __str__(self):
     return self.email