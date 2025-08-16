from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("list", views.post_list, name="post_list"),
]
