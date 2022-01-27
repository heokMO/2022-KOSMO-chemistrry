from django.urls import path

from reply import views

app_name = 'reply'

urlpatterns =[
    path('reply_write<int:post_seq>', views.reply_write, name='reply_write'),
    path('delete_reply/<int:reply_seq>/<int:post_seq>', views.delete_reply, name='delete_reply'),
]