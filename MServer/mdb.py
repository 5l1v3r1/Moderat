import os
import sys
import hashlib
from django.db.models import Q
from ModeratServer.models import *


class MDB:
    def __init__(self):
        moderatorsCount = Moderators.objects.all().count()
        if moderatorsCount is 0:
            self.createAdministrator('admin', '1234', 1)
            print 'Administrator Created (admin, 1234)'

    def setAllOffline(self):
        all_moderators = Moderators.objects.all()
        all_moderators.update(status=False)
        all_clients = Clients.objects.all()
        all_clients.update(status=False)

    def createClient(self, moderat_id, client_id, client_ip_address):
        query = Clients(pk=moderat_id, identifier=client_id, ip_address=client_ip_address,)
        query.save()

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

    def getPrivileges(self, username):
        moderator = Moderators.objects.get(username=username)
        if moderator.privileges:
            return moderator.privileges

    def setModeratorLastOnline(self, username):
        moderator = Moderators.objects.get(username=username)
        if moderator.privileges:
            moderator.last_online = datetime.now()

    def setModeratorStatus(self, username, state):
        moderator = Moderators.objects.get(username=username)
        if moderator.status:
            moderator.status = state
            moderator.save()

# # TESTS
# db = MDB()
