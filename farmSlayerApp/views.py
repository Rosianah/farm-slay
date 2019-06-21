from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from farmSlayerApp.forms import CustomUserCreationForm,CropForm
from django.shortcuts import render, redirect
from farmSlayerApp.models import Crop
import requests

# Create your views here.
from django.http import HttpResponse

# here is the homepage
@login_required(login_url='/farmSlayerApp/login')
def index(request):
	
	if request.user.is_farmer:
			if request.method == 'POST'and request.FILES['cropfile']:
				crop = Crop()
				crop.photo = request.FILES['cropfile']
				crop.user  = request.user
				crop.save()

				crop = Crop.objects.get(user=request.user)
				return render(request, 'farmSlayerApp/farmer.html',{'crop':crop})

			else:
				return render(request, 'farmSlayerApp/farmer.html')

		
	else:
		return render(request, 'farmSlayerApp/buyer.html')
	return render(request, 'farmSlayerApp/farmer.html',{'crop':crop})
def signup(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		
		
		if form.is_valid():
			form.save()
			return redirect('/farmSlayerApp/index')
			print(form)
		else:
				print(form.errors)
				return render(request, 'farmSlayerApp/signup.html')
	else:
		
		return render(request, 'farmSlayerApp/signup.html')




def weather(request):
	city= 'Kiambu'
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=10ad324f2d3dd05843342fa0efe8162f'
	city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
	weather = {
            
            'temperature' : city_weather['main']['temp'],
            
            
        }
	return HttpResponse(weather['temperature'])

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)