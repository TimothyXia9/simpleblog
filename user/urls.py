from django.urls import path
from . import views
from .views import UserListView

urlpatterns = [
    path("", views.index, name="index"),
    path("api/users/", UserListView.as_view(), name="user-list"),
    path("view-users/", views.view_all_users, name="view-all-users"),
    path("create-user/", views.create_user, name="create-user"),
]
