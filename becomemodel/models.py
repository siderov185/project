from django.db import models

class BecomeModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
