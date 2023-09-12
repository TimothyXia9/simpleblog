from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # 自定义字段

    def __str__(self):
        return self.username
