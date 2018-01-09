from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=128, unique=True)
    dates = models.ManyToManyField(User, through='DateVisited')

    def __str__(self):
        return self.name


class DateVisited(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_visited = models.DateTimeField(default=timezone.now, blank=True)
