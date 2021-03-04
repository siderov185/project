from django.db import models

class AboutMe(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.ImageField()
