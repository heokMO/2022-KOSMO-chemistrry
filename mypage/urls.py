from django.urls import path

from mypage import views

app_name = 'mypage'

urlpatterns =[
    path('myinfo', views.my_info, name='myinfo'),
    path('infoupdate', views.info_update, name='infoupdate'),
    path('mypost', views.my_post, name='mypost'),
    path('myreply', views.my_reply, name='myreply'),
]