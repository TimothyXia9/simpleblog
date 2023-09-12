from django.contrib import admin
from .models import BlogPost

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")  # 在列表中显示的字段
    ordering = ("created_at",)


# 注册你的模型和 Admin 类
admin.site.register(BlogPost, BlogPostAdmin)
