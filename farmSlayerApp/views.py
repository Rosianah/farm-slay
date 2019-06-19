from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# here is the homepage
def index(request):
    return render(request, 'farmSlayerApp/index.html')