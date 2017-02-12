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
        query = Moderators(username=username,
                           password=password_hash.hexdigest(),
                           privileges=privileges)
        query.save()

    def loginModerator(self, username, password):
        moderator = Moderators.objects.get(username=username)
        if moderator.username:
            password_hash = hashlib.md5()
            password_hash.update(password)
            if moderator.password == password_hash.hexdigest():
                return True
        return False

    def changePassword(self, username, new_password):
        moderator = Moderators.objects.get(moderator_id=username)
        if moderator.username:
            password = hashlib.md5()
            password.update(new_password)
            moderator.password = password.hexdigest()
            moderator.save()
        return False

    def changePrivileges(self, username, privilege):
        moderator = Moderators.objects.get(moderator_id=username)
        if moderator.privileges:
            moderator.privileges = privilege
            moderator.save()

    def deleteModerator(self, username):
        moderator = Moderators.objects.get(moderator_id=username)
        if moderator.username:
            moderator.delete()

# TESTS
db = MDB()
