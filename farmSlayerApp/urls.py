from django.urls import path
from django.contrib.auth.views import LoginView


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather', views.weather, name='weather'),
    path('signup', views.signup, name='signup'),
    path('login', LoginView.as_view(template_name='/farmSlayerApp/login.html'), name="login"),
]