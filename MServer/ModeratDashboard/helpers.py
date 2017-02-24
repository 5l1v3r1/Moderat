import datetime, sys
from ModeratServer.models import *
from django.db.models import Count


def get_uptime():
    if sys.platform.startswith('win'):
        uptime = 'Windows Not Supported Yet!!!'
    else:
        with open('/proc/uptime') as f:
            boot = datetime.timedelta(seconds=float(f.readline().split()[0])).total_seconds()
            uptime = '{} days, {} hours, {} minutes, {} seconds'.format(
                boot // 86400, boot // 3600 % 24, boot // 60 % 60, boot % 60)
    return uptime


def get_clients_moderators_informations():
    total_clients = Clients.objects.all().count()
    online_clients = Clients.objects.filter(status=True).count()
    offline_clients = total_clients - online_clients
    total_moderators = Moderators.objects.all().count()
    online_moderators = Moderators.objects.filter(status=True).count()
    offline_moderators = total_moderators - online_moderators
    return total_clients, online_clients, offline_clients, total_moderators, online_moderators, offline_moderators


def get_logs_information():
    total_screenshots = Screenshots.objects.all().count()
    total_keylogs = Keylogs.objects.all().count()
    total_audios = Audios.objects.all().count()
    return total_screenshots, total_keylogs, total_audios


def get_clients_geo_location():
    return Clients.objects.values('country', 'country_code').order_by('country').annotate(count=Count('country'))
