from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register("blogs", views.BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api/blogs/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="blog-delete"
    ),
]
