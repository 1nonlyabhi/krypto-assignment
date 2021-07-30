from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Alert(models.Model):
    targetPrice = models.IntegerField()
    status = models.BooleanField(default=True)
    holder = models.ForeignKey(User, on_delete=models.CASCADE)