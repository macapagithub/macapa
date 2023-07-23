from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True)
    # summary  #with a llm you can add a resume to your post.

    def __str__(self):
        return self.title
    
    # def summary(self):
    #     return self.body[:100]
    #     return self.summary (thinking about it)
