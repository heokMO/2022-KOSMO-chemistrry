from django.urls import path

from mypage import views

app_name = 'mypage'

urlpatterns =[
    path('myinfo', views.myinfo, name='myinfo'),
    path('mypost', views.mypost, name='mypost'),
    path('myreply', views.myreply, name='myreply'),
    ]