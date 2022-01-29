from django.urls import path

from mypage import views

app_name = 'mypage'

urlpatterns =[
    path('myinfo', views.my_info, name='myinfo'),
    path('infoupdate', views.info_update, name='infoupdate'),
    path('my_post', views.my_post, name='my_post'),
    path('my_reply', views.my_reply, name='my_reply'),
]