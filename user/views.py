from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

# Create your views here.


def index(request):
    return render(
        request, "index.html", {"index_url": staticfiles_storage.url("index.html")}
    )


def view_all_users(request):
    # 获取所有用户数据
    users = CustomUser.objects.all()
    return render(request, "view_users.html", {"users": users})


def create_user(request):
    return render(request, "create_user.html")


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
