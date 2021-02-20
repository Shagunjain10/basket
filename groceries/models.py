from django.db import models
from django.utils import timezone

# Create your models here.


class GroceryItem(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500, default='')
    createdAt = models.DateTimeField(default=timezone.now)
    price = models.PositiveIntegerField(default=0)
