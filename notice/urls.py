from django.urls import path

from notice import views

app_name = 'notice'

urlpatterns =[
    path('showpostwrite', views.show_post_write, name='showpostwrite'),
    path('postinsert', views.post_write, name='postinsert'),
    path('showpostlist', views.show_post_list, name='showpostlist'),
    path('showpostdetail/<int:post_seq>', views.show_post_detail, name='showpostdetail'),
    path('showpostupdate/<int:post_seq>', views.show_post_update, name='showpostupdate'),
    path('postupdate<int:post_seq>', views.post_update, name='postupdate'),
    path('postdelete<int:post_seq>', views.post_delete, name='postdelete'),
]