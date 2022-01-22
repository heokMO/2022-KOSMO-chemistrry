from django.urls import path

from my_page import views

app_name = 'mypage'

urlpatterns = [
    path('myinfo', views.myinfo, name='myinfo'),
    path('postreply', views.postreply, name='postReply'),
]