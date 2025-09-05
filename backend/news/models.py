import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    uuid = models.CharField(max_length=200, primary_key=True, default="no-uuid")
    title = models.CharField(max_length=200, default="no title")
    description = models.TextField(default="no description")
    keywords = models.TextField(default="no keywords")
    snippet = models.TextField(default="no snippet")
    url = models.URLField(max_length=200, default='https://www.google.com')
    language = models.CharField(max_length=50, default="en")
    published_date = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=200, default="unknown")
    categories = models.JSONField(default=list, blank=True)
    locale = models.CharField(max_length=50, default="us")
    def __str__(self):
        return self.title