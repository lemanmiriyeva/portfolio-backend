from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'profile', views.ProfileViewSet)

urlpatterns = [
    path('', views.api_overview),
    path('', include(router.urls)),
]
