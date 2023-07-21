# speaker/models.py
from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='speakers/', default='100')  # Set default value to an empty string
    website = models.URLField(blank=True)
    twitter_handle = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
