from django.urls import path

from delivery import views

app_name = 'delivery'

urlpatterns =[
    path('list',views.list,name='list'),
    path('write',views.write,name='write'),
]