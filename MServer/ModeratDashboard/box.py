# -*- coding: utf-8 -*-
# dashboard/boxes.py

from __future__ import unicode_literals
import platform
import psutil
import datetime
import sys
import subprocess
from datetime import timedelta
from django.utils.translation import ugettext as _
from suit_dashboard.box import Box, Item
from ModeratServer.models import *

class LogsInformation(Box):

    screenshotsCount = Screenshots.objects.all().count()
    keylogsCount = Keylogs.objects.all().count()
    audiosCount = Audios.objects.all().count()

    def get_title(self):
        return _('Total Logs {}'.format(self.screenshotsCount + self.keylogsCount + self.audiosCount))

    def get_description(self):
        return ''

    def get_items(self):
        chart_options = {
            'chart': {
                'type': 'pie',
                'height': 300,
            },
            'title': {
                'text': ''
            },

            'series': [{
                'name': 'Logs',
                'colorByPoint': 'true',
                'y': 40,
                'data': [{
                    'name': 'Screenshots ({})'.format(self.screenshotsCount),
                    'color': '#e67e22',
                    'y': self.screenshotsCount
                }, {
                    'name': 'Keylogs ({})'.format(self.keylogsCount),
                    'color': '#3498db',
                    'y': self.keylogsCount
                }, {
                    'name': 'Audios ({})'.format(self.audiosCount),
                    'color': '#9b59b6',
                    'y': self.audiosCount
                }],
            }]
        }

        # Create the chart item
        item_chart = Item(
            html_id='highchart-logs',
            value=chart_options,
            display=Item.AS_HIGHCHARTS)

        # Return the list of items
        return [item_chart,]

class ClientsInformation(Box):

    clients_count = Clients.objects.all().count()
    online_clients_count = Clients.objects.filter(status=True).count()
    print online_clients_count
    offline_clients_count = clients_count - online_clients_count

    def get_title(self):
        return _('Total Clients {}'.format(self.clients_count))

    def get_description(self):
        return ''

    def get_items(self):
        chart_options = {
            'chart': {
                'type': 'pie',
                'height': 300,
            },
            'title': {
                'text': ''
            },

            'series': [{
                'name': 'Clients',
                'colorByPoint': 'true',
                'y': self.clients_count,
                'data': [{
                    'name': 'Online Clients ({})'.format(self.online_clients_count),
                    'color': '#1abc9c',
                    'y': self.online_clients_count
                }, {
                    'name': 'Offline Clients ({})'.format(self.offline_clients_count),
                    'color': '#e74c3c',
                    'y': self.offline_clients_count
                }],
            }]
        }

        # Create the chart item
        item_chart = Item(
            html_id='highchart-clients',
            value=chart_options,
            display=Item.AS_HIGHCHARTS)

        # Return the list of items
        return [item_chart,]


class BoxMachine(Box):
    def get_title(self):
        return _('Machine')

    def get_description(self):
        return ''

    # The get_items function is the main function here. It will define
    # what are the contents of the box.
    def get_items(self):
        if sys.platform.startswith('win'):
            cmd = "net statistics server"
            p = subprocess.Popen(cmd, shell=True,
                                 stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            (child_stdin, child_stdout) = (p.stdin, p.stdout)
            lines = child_stdout.readlines()
            child_stdin.close()
            child_stdout.close()
            lines = [line.strip() for line in lines if line.strip()]
            date, time, ampm = lines[1].split()[2:5]
            m, d, y = [int(v) for v in date.split('/')]
            H, M, _tmp = [int(v) for v in time.split(':')]
            if ampm.lower() == 'pm':
                H += 12
            now = datetime.datetime.now()
            then = datetime.datetime(y, m, d, H, M)
            diff = now - then
            uptime = diff
        else:
            with open('/proc/uptime') as f:
                s = timedelta(seconds=float(f.readline().split()[0])).total_seconds()
                uptime = _('%d days, %d hours, %d minutes, %d seconds') % (
                    s // 86400, s // 3600 % 24, s // 60 % 60, s % 60)

        # Create a first item (box's content) with the machine info
        item_info = Item(
            html_id='sysspec', name=_('System specifications'),
            display=Item.AS_TABLE,
            # Since we use AS_TABLE display, value must be a list of tuples
            value=(
                (_('Hostname'), platform.node()),
                (_('System'), '%s, %s, %s' % (
                    platform.system(),
                    ' '.join(platform.linux_distribution()),
                    platform.release())),
                (_('Architecture'), ' '.join(platform.architecture())),
                (_('Python version'), platform.python_version()),
                (_('Uptime'), uptime)
            ),
            classes='table-bordered table-condensed '
                    'table-hover table-striped'
        )

        # Retrieve RAM and CPU data
        ram = psutil.virtual_memory().percent
        cpu = psutil.cpu_percent()

        # Green, orange, red or grey color for usage/idle
        green, orange, red, grey = '#00FF38', '#FFB400', '#FF3B00', '#EBEBEB'

        ram_color = green  # default
        if ram >= 75:
            ram_color = red
        elif ram >= 50:
            ram_color = orange

        cpu_color = green  # default
        if cpu >= 75:
            cpu_color = red
        elif cpu >= 50:
            cpu_color = orange

        # Now create a chart to display CPU and RAM usage
        chart_options = {
            'chart': {
                'type': 'bar',
                'height': 200,
            },
            'title': {
                'text': _('RAM and CPU usage')
            },
            'xAxis': {
                'categories': [_('CPU usage'), _('RAM usage')]
            },
            'yAxis': {
                'min': 0,
                'max': 100,
                'title': {
                    'text': _('Percents')
                }
            },
            'tooltip': {
                'percentageDecimals': 1
            },
            'legend': {
                'enabled': False
            },
            'plotOptions': {
                'series': {
                    'stacking': 'normal'
                }
            },
            'series': [{
                'name': _('CPU idle'),
                'data': [{'y': 100 - cpu, 'color': grey}, {'y': 0}],
            }, {
                'name': _('CPU used'),
                'data': [{'y': cpu, 'color': cpu_color}, {'y': 0}],
            }, {
                'name': _('RAM free'),
                'data': [{'y': 0}, {'y': 100 - ram, 'color': grey}],
            }, {
                'name': _('RAM used'),
                'data': [{'y': 0}, {'y': ram, 'color': ram_color}],
            }]
        }

        # Create the chart item
        item_chart = Item(
            html_id='highchart-machine-usage',
            name=_('Machine usage'),
            value=chart_options,
            display=Item.AS_HIGHCHARTS)

        # Return the list of items
        return [item_info, item_chart]