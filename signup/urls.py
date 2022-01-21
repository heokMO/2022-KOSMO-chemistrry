from django.urls import path

from signup import views

app_name = 'signup'

urlpatterns = [
    path("", views.login),
    path("mainpage", views.mainpage),
    path("signup", views.memberjoin, name='signup'),
]