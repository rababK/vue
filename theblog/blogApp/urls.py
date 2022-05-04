from .views import allPosts


from django.urls import path, include
from .views import allPosts

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", allPosts, "posts")

urlpatterns = [
    path("api/", include(router.urls), name="api"),
]
