from django.db import models

class PhotoSessions(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    photos = models.ImageField()
