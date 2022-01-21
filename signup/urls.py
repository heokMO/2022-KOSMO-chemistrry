from django.urls import path

from signup import views

urlpatterns = [
    path("", views.login),
    path("mainpage", views.mainpage),
    path("memberjoin", views.memberjoin),
]