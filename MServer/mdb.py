import os
import sys
import hashlib
from django.db.models import Q

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Server.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from ModeratServer.models import *


class MDB:
    def __init__(self):
        moderatorsCount = Moderators.objects.all().count()
        if moderatorsCount is 0:
            self.createAdministrator('admin', '1234', 1)
            print 'Administrator Created (admin, 1234)'

    def createAdministrator(self, username, password, privileges):
        password_hash = hashlib.md5()
        password_hash.update(password)
        query = Moderators(moderator_id=username,
                           moderator_password=password_hash.hexdigest(),
                           moderator_privs=privileges)
        query.save()


# TESTS
db = MDB()
