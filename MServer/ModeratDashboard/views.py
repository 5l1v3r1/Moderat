from __future__ import unicode_literals
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from suit_dashboard.layout import Grid, Row, Column
from suit_dashboard.views import DashboardView
from suit_dashboard.box import Box
from ModeratDashboard.box import BoxMachine, ClientsInformation, LogsInformation

class HomeView(DashboardView):
    template_name = 'main.html'
    crumbs = (
        {'url': 'admin:index', 'name': _('Home')},
    )
    grid = Grid(
        Row(
            Column(BoxMachine(), width=4),
            Column(ClientsInformation(), width=4),
            Column(LogsInformation(), width=4)
            ),
               )