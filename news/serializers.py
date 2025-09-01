from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'published_date', 'source', 'url']