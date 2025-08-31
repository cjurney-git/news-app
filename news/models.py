import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=200)
    url = models.URLField(max_length=200, default='https://www.google.com')
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)