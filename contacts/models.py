from django.db import models

class Contacts(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField()
    description = models.CharField(max_length=50)
    text = models.TextField()
