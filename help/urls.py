from django.urls import path

from help import views

app_name = 'help'

urlpatterns = [
    # 기존에는 url을 다 써주는 방식이었다면 namespace는 앱이름이 help인 앱을 찾아 name에 값으로 연결 시켜준다.
    # 앱 이름이 help인 앱을 찾아서 name이 showpostwrite인 애를 찾아서 들어간다.
    # url에 name를 붙여주는 것 = name 스페이스는 앱에 url을 지정해주는
    path('showpostwrite', views.show_post_write, name='showpostwrite'),
    path('postinsert', views.post_write, name='postinsert'),
    path('showpostlist', views.show_post_list, name='showpostlist'),
    path('showpostdetail/<int:post_seq>', views.show_post_detail, name='showpostdetail'),
    # <int:post_seq>가 있으면 url뒤에 post_seq가 붙는 형태가 된다 --> /notice/showpostdetail/1
    path('showpostupdate/<int:post_seq>', views.show_post_update, name='showpostupdate'),
    path('postupdate<int:post_seq>', views.post_update, name='postupdate'),
    path('postdelete/<int:post_seq>', views.post_delete, name='postdelete'),
]