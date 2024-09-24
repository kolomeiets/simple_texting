import datetime
import requests
from django.db import models
from django.utils import timezone
from authentication.models import User
from django.conf import settings

class Group(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def send_invitation(self, user):
        message = f"Hi { user.first_name }, welcome to the chat group { self.name }. You can reply to send messages back to chat!"
        json = {
            "contactPhone": str(user.phone_number),
            "mode": "SINGLE_SMS_STRICTLY",
            "text": message
        }
        response = requests.post(
            "https://api-app2.simpletexting.com/v2/api/messages",
            headers={"Authorization": f"Bearer {settings.SIMPLE_TEXTING_API_TOKEN}"},
            json=json
        )


class GroupUsers(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groups_joined')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group.name