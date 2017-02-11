from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.
class Moderators(models.Model):
    moderator_id = models.CharField(max_length=100)
    moderator_password = models.CharField(max_length=100)
    moderator_privs = models.IntegerField(max_length=1)
    moderator_status = models.BooleanField(default=False)
    moderator_last_online = models.DateTimeField(default=datetime.now())


class Clients(models.Model):
    moderator_id = models.CharField(max_length=100)
    client_id = models.CharField(max_length=100)
    client_alias = models.CharField(max_length=100)
    client_ipAddress = models.CharField(max_length=100)
    client_last_connected = models.DateTimeField(default=datetime.now())
    client_status = models.BooleanField(default=False)