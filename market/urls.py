from django.urls import path

from market import views

urlpatterns = [
    path('bb_write',views.bb_write),
    path('meminsert',views.meminsert),
    path('list', views.list, name='list'),
    path('write', views.write, name='write'),
]