from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('', views.logout, name='logout'),
]