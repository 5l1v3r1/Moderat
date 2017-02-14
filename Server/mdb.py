from django.conf import settings

settings.configure()

from Server.ModeratServer.models import *

class MDB:


    def __init__(self):

        moderatorsCount = Moderators.objects.all().count()
        print moderatorsCount


# TESTS
db = MDB()