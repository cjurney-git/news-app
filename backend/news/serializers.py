from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['uuid', 'title', 'description', 'keywords', 'snippet', 'published_date', 'source', 'image_url', 'url', 'language', 'categories', 'locale']