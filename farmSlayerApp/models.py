from django.db import models

# Create your models here.
## users/modles.py

from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
  # add additional fields in here

  location = models.CharField(max_length=100, default='')
  phoneNumber = models.IntegerField(default=0)
  is_farmer = models.BooleanField(default=False)



class Crop (models.Model):
	crop_id = models.AutoField(primary_key=True)
	photo = models.ImageField(upload_to='media')
	"""
	pest = models.CharField(max_length=100, default='')
	quality = models.CharField(max_length=100, default='')
	"""
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


	


