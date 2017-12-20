from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Location(models.Model):
    name = models.CharField(max_length=128, unique=True)
    dates = models.ManyToManyField(User, through='DateVisited')

    def __str__(self):
        return self.name


class DateVisited(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_visited = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.date_visited
