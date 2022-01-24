from django.urls import path

from delivery import views

app_name = 'delivery'

urlpatterns =[
    path('showpostlist',views.show_post_list,name='showpostlist'),
    path('showpostwrite',views.show_post_write,name='showpostwrite'),
    path('showpostdetail',views.show_post_detail,name='showpostdetail'),
]