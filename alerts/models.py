from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Alert(models.Model):
    targetPrice = models.IntegerField() # price created by user to get an alert
    created = models.BooleanField(default=False)    # shows activated alert
    deleted = models.BooleanField(default=False)    # shows deleted alert
    triggered = models.BooleanField(default=False)  # shows triggered alert after acheiving targetPrice
    holder = models.ForeignKey(User, on_delete=models.CASCADE)  # connecting to the Django default User 