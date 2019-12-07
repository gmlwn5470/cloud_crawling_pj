from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    photo = models.ImageField(blank=True)
   # created_date = models.DateTimeField(default=timezone.now)

    def show(self):
        self.save()
        
    def __str__(self):
        return self.title

