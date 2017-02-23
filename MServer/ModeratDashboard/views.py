# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.views.generic import TemplateView
import psutil, helpers, platform


class HomeView(TemplateView):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        totalClients, onlineClients, offlineClients, totalModerators, onlineModerators, offlineModerators = \
            helpers.get_clients_moderators_informations()
        totalScreenshots, totalKeylogs, totalAudios = helpers.get_logs_information()
        context['machine'] = {
            'cpu_percent':  psutil.cpu_percent(interval=0),
            'memory_usage': psutil.virtual_memory().percent,
            'uptime': helpers.get_uptime(),
            'hostname': platform.node(),
            'system': '%s, %s, %s' % (
                    platform.system(),
                    ' '.join(platform.linux_distribution()),
                    platform.release()),
            'architecture': ' '.join(platform.architecture()),
            'python_version': platform.python_version(),
        }
        context['clients'] = {
            'total': totalClients,
            'online': onlineClients,
            'offline': offlineClients,
        }
        context['moderators'] = {
            'total': totalModerators,
            'online': onlineModerators,
            'offline': offlineModerators
        }
        context['screenshots'] = {
            'total': totalScreenshots,
        }
        context['keylogs'] = {
            'total': totalKeylogs,
        }
        context['audios'] = {
            'total': totalAudios,
        }
        context['clientsGeo'] = helpers.get_clients_geo_location()
        return self.render_to_response(context=context)