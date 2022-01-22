from django.urls import path

from notice import views

app_name = 'notice'

urlpatterns =[
    path('list',views.list,name='list'),
    path('write',views.write,name='write'),
]