import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Server.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from twisted.internet import reactor
from twisted.internet.error import CannotListenError
from serverCore import ModeratServerFactory

CLIENTS_PORT = 443

try:
    from twisted.python import log
    import sys
    # Default Twisted Logging
    #log.startLogging(sys.stdout)
    factory = ModeratServerFactory()
    reactor.listenTCP(CLIENTS_PORT, factory)
    #reactor.listenTCP(MODERATORS_PORT, ModeratServerFactory())
    reactor.run()
except CannotListenError:
    print '[*SERVER] PORT ALREADY USED'
    os._exit(1)
