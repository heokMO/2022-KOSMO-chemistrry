from django.urls import path

from help import views

app_name = 'help'

urlpatterns =[
    path('list',views.list,name='list'),
    path('write',views.write,name='write'),
]