from django.urls import path

from member import views

urlpatterns = [
    path("memberInsert", views.memberInsert),
]