from django.urls import path

from signup import views

app_name = 'signup'

urlpatterns = [
    path("", views.login),
    path("signup", views.signup, name='signup'),
    path("signup2", views.signup2, name='signup2'),
    path("last_signup<int:mem_seq>", views.last_signup, name='last_signup')
]
