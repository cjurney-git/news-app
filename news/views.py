from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response   
from .models import Article
from .serializers import ArticleSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the news index.")

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
