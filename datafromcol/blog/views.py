from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def inicio(request):
    contexto = {"nombre": "Home Page"}
    return render(request, "home/home.html", contexto)
