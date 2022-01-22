from django.urls import path

from signup import views

app_name = 'signup'

urlpatterns = [
    path("", views.login),
    path("signup", views.signup, name='signup'),
]
