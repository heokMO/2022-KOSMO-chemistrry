from django.urls import path

from help import views

app_name = 'help'

urlpatterns = [
    path('showpostlist', views.show_post_list, name='showpostlist'),
    path('showpostwrite', views.show_post_write, name='showpostwrite'),
    path('showpostdetail/<int:post_seq>', views.show_post_detail, name='showpostdetail'),
    path('showpostupdate/<int:post_seq>', views.show_post_update, name='showpostupdate'),
    path('postupdate', views.post_update, name='postupdate'),
    path('postdelete/<int:post_seq>', views.post_delete, name='postdelete'),
]