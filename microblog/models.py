from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
