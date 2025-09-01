from django.urls import include, path

from rest_framework import routers, serializers, viewsets
from rest_framework.renderers import JSONRenderer
from .views import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
]