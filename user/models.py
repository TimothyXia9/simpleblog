from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 基本字段
    email = models.EmailField(unique=True)
    # 如果你希望用户有昵称而不是使用用户名显示，可以添加一个昵称字段
    nickname = models.CharField(max_length=255, blank=True, null=True)
    # 如果需要用户头像，可以添加一个头像字段
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # 笔记相关字段
    # 例如，用户可以有一个简介字段，描述一些关于用户自己的信息
    bio = models.TextField(blank=True, null=True)