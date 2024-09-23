import datetime

from django.db import models
from django.utils import timezone
from authentication.models import User

class Group(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GroupUsers(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.group.name