from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from farmSlayerApp.models import CustomUser,Crop
# Create your models here.
## users/modles.py
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUserCreationForm(UserCreationForm):
  # add additional fields in here

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username','email','password1','password2','location','phoneNumber','is_farmer')
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class CropForm(ModelForm):
    class Meta:
        model = Crop

        #fields = ('photo','media_description','is_gallery')
        exclude = () 
"""
class Crop (forms.Form):
	crop_id = models.AutoField(primary_key=True)
	plant_date = models.DateField()
	harvest_date = models.DateField()

class Farmer(models.Model):

	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
	crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

"""