import hashlib
import datetime
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

    def createClient(self, username, identifier, client_ip_address):
        moderator = Moderators.objects.get(username=username)
        if moderator:
            client_exists = Clients.objects.filter(identifier=identifier)
            if not client_exists:
                query = Clients(moderator_id=moderator, identifier=identifier, ip_address=client_ip_address,)
                query.save()

    def getAllClients(self):
        moderators = Moderators.objects.filter(privileges=1)
        all_moderators_id = moderators.values_list('pk', flat=True).distinct()
        return Clients.objects.all().exclude(pk__in=all_moderators_id)

    def getClients(self, moderator):
        clients = Clients.objects.filter(pk=moderator.pk)
        return clients

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

    def getOfflineClients(self, moderator):
        clients = Clients.objects.filter(moderator_id=moderator.pk, status=False)
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
        if client:
            client.status = status
            client.save()

    def setClientLastOnline(self, identifier):
        client = Clients.objects.get(identifier=identifier)
        if client:
            client.last_connected = datetime.now()


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
        if moderator:
            password_hash = hashlib.md5()
            password_hash.update(password)
            if moderator.password == password_hash.hexdigest():
                return True
        return False

    def changePassword(self, username, new_password):
        moderator = Moderators.objects.get(username=username)
        if moderator:
            password = hashlib.md5()
            password.update(new_password)
            moderator.password = password.hexdigest()
            moderator.save()
        return False

    def changePrivileges(self, username, privilege):
        moderator = Moderators.objects.get(username=username)
        if moderator:
            moderator.privileges = privilege
            moderator.save()

    def deleteModerator(self, username):
        moderator = Moderators.objects.get(username=username)
        if moderator:
            moderator.delete()

    def isAdministrator(self, username):
        moderator = Moderators.objects.get(username=username)
        if moderator:
            return moderator.privileges

    def setModeratorLastOnline(self, username):
        moderator = Moderators.objects.get(username=username)
        if moderator:
            moderator.last_online = datetime.now()
            moderator.save()

    def setModeratorStatus(self, username, state):
        moderator = Moderators.objects.get(username=username)
        if moderator:
            moderator.status = state
            moderator.save()

    def getModerator(self, username):
        return Moderators.objects.get(username=username)

    def getModerators(self):
        return Moderators.objects.all()
