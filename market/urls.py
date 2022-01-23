from django.urls import path

from market import views

app_name = 'market'

urlpatterns = [
    path('postinsert',views.postinsert),
    path('showpostlist', views.show_post_list, name='showpostlist'),
    path('showpostwrite', views.show_post_write, name='showpostwrite'),
]