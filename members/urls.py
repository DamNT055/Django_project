from django.urls import path
from . import views

urlpatterns = [
    path("members", views.members, name="members"),
    path("members/list", views.post_list, name="members list"),
]
