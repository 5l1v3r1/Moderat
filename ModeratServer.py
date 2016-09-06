from twisted.internet import reactor
from Server.ModeratServer import *

CLIENTS_PORT = 4434
MODERATORS_PORT = 1313

reactor.listenTCP(CLIENTS_PORT, ModeratServerFactory())
reactor.listenTCP(MODERATORS_PORT, ModeratServerFactory())
reactor.run()
