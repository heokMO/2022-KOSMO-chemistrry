from django.urls import path

from post import views

app_name = 'post'

urlpatterns = [
    path('show_post_detail<int:post_seq>', views.show_post_detail, name='show_post_detail')
]