from django.urls import path

from mypage import views

urlpatterns = [
    path("", views.login),
    path("mainpage", views.mainpage),
    path("memberjoin", views.memberjoin),
]