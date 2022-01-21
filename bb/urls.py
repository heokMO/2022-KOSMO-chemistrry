from django.urls import path

from bb import views

urlpatterns = [
    path('help_bb',views.help_bb),
    path('help_write',views.help_write),
    path('notice_bb',views.notice_bb),
    path('notice_write',views.notice_write),
    path('help_list',views.help_list),
    path('notice_list',views.notice_list),


]