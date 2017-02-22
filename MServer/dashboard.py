"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'MServer.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name
from ModeratServer.models import *

import psutil

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.Group(
            column=1,
            collapsible=True,
            children=[
                modules.LinkList(
                    _('Perfomance & Statistic'),
                    column=1,
                    collapsible=True,
                    pre_content='''
<html>
      <head>
        <!--Load the AJAX API-->
        <script type="text/javascript" src="https://www.google.com/jsapi"></script>
        <script type="text/javascript">

          // Load the Visualization API and the piechart package.
          google.load('visualization', '1.0', {'packages':['corechart']});
          google.load('visualization', '1.0', {'packages':['gauge']});


          // Set a callback to run when the Google Visualization API is loaded.
          google.setOnLoadCallback(drawChart);

          // Callback that creates and populates a data table,
          // instantiates the pie chart, passes in the data and
          // draws it.
          function drawChart() {

            // Create the data table.
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Topping');
            data.addColumn('number', 'Slices');
            data.addRows([
              ['CPU', %s],
              ['Memory', %s]
            ]);
            // Create the data table.
            var data2 = new google.visualization.DataTable();
            data2.addColumn('string', 'Topping');
            data2.addColumn('number', 'Slices');
            data2.addRows([
              ['Online Clients', %s],
              ['Offline Clients', %s]
            ]);

            // Set chart options
            var options = {'width':400,
                           'height':300};
            // Set chart options
            var options2 = {'title':'Total Clients: %s',
                           'width':550,
                           'height':300};

            // Instantiate and draw our chart, passing in some options.
            var chart = new google.visualization.Gauge(document.getElementById('chart_div'));
            chart.draw(data, options);
            var chart2 = new google.visualization.PieChart(document.getElementById('chart_div2'));
            chart2.draw(data2, options2);

          }
        </script>
      </head>

      <body>
        <!--Divs that will hold the charts-->
        <div id="chart_div"></div>
        <div id="chart_div2"></div>
        <div id="chart_div3"></div>
      </body>
    </html>
                    ''' % (psutil.cpu_percent(interval=1),
                           psutil.virtual_memory().percent,
                           Clients.objects.filter(status=True).count(),
                           Clients.objects.filter(status=False).count(),
                           Clients.objects.all().count()),
                ),
            ]
        ))
        
        # append a group for "Administration" & "Applications"
        self.children.append(modules.Group(
            _('Administration & Applications'),
            column=2,
            collapsible=True,
            children = [
                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=True,
                    models=('django.contrib.*',),
                ),
                modules.AppList(
                    _('Applications'),
                    column=1,
                    css_classes=('collapse closed',),
                    exclude=('django.contrib.*',),
                )
            ]
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))
        
        # append a feed module
        self.children.append(modules.Feed(
            _('Latest ModeRat Updates'),
            column=3,
            feed_url='https://github.com/Swordf1sh/Moderat/commits/dev.atom',
            limit=5
        ))


