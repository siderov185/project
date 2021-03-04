from django.db import models

class Index(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


