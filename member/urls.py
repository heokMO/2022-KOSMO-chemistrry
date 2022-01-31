from django.urls import path

from member import views

app_name = 'member'

urlpatterns = [
    path("member_insert", views.member_insert, name='insert'),
    path("login", views.login, name='login'),
]