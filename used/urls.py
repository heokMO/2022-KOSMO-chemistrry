from django.urls import path
from used import views



urlpatterns = [
    path('used/', views.used),

]