import os
import sys
import hashlib
from django.db.models import Q
from ModeratServer.models import *


class MDB:
    def __init__(self):
        moderatorsCount = Moderators.objects.all().count()
        if moderatorsCount is 0:
            self.createModerator('admin', '1234', 1)
            print 'Administrator Created (admin, 1234)'

    def setAllOffline(self):
        all_moderators = Moderators.objects.all()
        all_moderators.update(status=False)
        all_clients = Clients.objects.all()
        all_clients.update(status=False)

    def createClient(self, moderat_id, client_id, client_ip_address):
        query = Clients(pk=moderat_id, identifier=client_id, ip_address=client_ip_address,)
        query.save()

    def getAllClients(self):
        return Clients.objects.all()

    def getClients(self, username):
        all_clients = Clients.objects.filter(pk=self.getModeratorPk(username))
        return all_clients

    def getClientAlias(self, identifier):
        client = Clients.objects.get(identifier=identifier)
        if client.alias:
            return client.alias

    def getClientNote(self, identifier):
        client = Clients.objects.get(identifier=identifier)
        if client.note:
            return client.note

    def getClientIPAddress(self, identifier):
        client = Clients.objects.get(identifier=identifier)
        if client.ip_address:
            return client.ip_address

    def getClientLastOnline(self, identifier):
        client = Clients.objects.get(identifier=identifier)
        if client.last_online:
            return client.last_online

    def getClientModerator(self, identifier):
        client = Clients.objects.get(identifier=identifier)
        if client.moderator_id:
            return client.moderator_id

    def getOfflineClients(self, username):
        clients = Clients.objects.filter(moderator_id=self.getModeratorPk(username),
                                         status=False)
        return clients

    def getAllOfflineClients(self):
        return Clients.objects.filter(status=False)

    def setClientAlias(self, identifier, alias):
        client = Clients.objects.get(identifier=identifier)
        if client.alias:
            client.alias = alias
            client.save()

    def setClientNote(self, identifier, note):
        client = Clients.objects.get(identifier=identifier)
        if client.note:
            client.note = note
            client.save()

    def setClientModerator(self, identifier, username):
        moderator = Moderators.objects.get(username=username)
        if moderator:
            client = Clients.objects.get(identifier=identifier)
            if client.identifier:
                client.moderator_id = moderator.pk
                client.save()
                return
        return False

    def setClientStatus(self, identifier, status):
        client = Clients.objects.get(identifier=identifier)
        if client.status:
            client.status = status
            client.save()

    def deleteClient(self, identifier):
        client = Clients.objects.get(identifier=identifier)
        if client.identifier:
            client.delete()

    def clientIsOnline(self, identifier):
        client = Clients.objects.get(identifier=identifier)
        return client.status

    def createModerator(self, username, password, privileges):
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
        if moderator:
            return moderator.privileges

    def setModeratorLastOnline(self, username):
        moderator = Moderators.objects.get(username=username)
        if moderator:
            moderator.last_online = datetime.now()

    def setModeratorStatus(self, username, state):
        moderator = Moderators.objects.get(username=username)
        if moderator:
            moderator.status = state
            moderator.save()

    def getModeratorPk(self, username):
        return Moderators.objects.get(username=username).pk

    def getModerators(self):
        return Moderators.objects.all()
