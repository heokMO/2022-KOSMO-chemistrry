from django.urls import path

from used import views

urlpatterns = [
    path('bb_write',views.bb_write),
    path('meminsert',views.meminsert),
]