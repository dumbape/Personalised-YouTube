from django.contrib import admin
from . import models

class APIFetchAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.fetchAPI == True:
            return ('fetchAPI', 'searchQuery', 'apiKey', 'fetchInterval', )
        else:
            return self.readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(models.Video)
admin.site.register(models.APIFetch, APIFetchAdmin)
