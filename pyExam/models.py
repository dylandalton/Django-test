import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    heading_text = models.CharField(max_length=40)
    date_and_time = models.DateTimeField('date published')
    story_text = models.CharField(max_length=200)
    def __str__(self):
        return self.heading_text
    def was_published_recently(self):
        return self.date_and_time >= timezone.now() - datetime.timedelta(days=1)

class New_Article(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_text = models.CharField(max_length=200)
    def __str__(self):
        return self.user_text
