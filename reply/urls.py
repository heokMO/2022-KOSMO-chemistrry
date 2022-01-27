from django.urls import path

from reply import views

app_name = 'reply'

urlpatterns = [
    path('replyinsert/<int:post_seq>',views.reply_insert, name='replyinsert')
]