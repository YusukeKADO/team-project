from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    like = models.IntegerField(default=0)

    def publish(self):
        self.posted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Media(models.Model):
    picture = models.ImageField(
        verbose_name = 'picture',
        upload_to = 'images/', 
        null = True,
    )
    posted_at = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.posted_at = timezone.now()
        self.save()