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
	plant_date = models.DateField()
	harvest_date = models.DateField()

class Farmer(models.Model):

	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
	crop = models.ForeignKey(Crop, on_delete=models.CASCADE)


