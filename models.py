from django.db import models

class Product(models.model):
  title = models.CharField(max_length=255)
  description = models.TextField()


