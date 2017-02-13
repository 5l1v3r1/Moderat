from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.
class Moderators(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    privileges = models.IntegerField(max_length=1)
    status = models.BooleanField(default=False)
    last_online = models.DateTimeField(default=datetime.now())


class Clients(models.Model):
    moderator_id = models.ForeignKey(Moderators)
    identifier = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    last_connected = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=False)