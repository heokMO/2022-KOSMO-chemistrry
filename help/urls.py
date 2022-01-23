from django.urls import path

from help import views

app_name = 'help'

urlpatterns =[
    path('showpostlist',views.show_post_list,name='showpostlist'),
    path('showpostwrite',views.show_post_write,name='showpostwrite'),
]