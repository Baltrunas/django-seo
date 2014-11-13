from django.contrib import admin

from .models import Data
from .models import Redirect
from .models import SiteSettings


class DataAdmin(admin.ModelAdmin):
	list_display = ['title', 'header', 'url', 'public', 'created_at']
	search_fields = ['title', 'header', 'url', 'public', 'created_at']
	list_filter = ['public', 'sites']
	list_editable = ['public']

admin.site.register(Data, DataAdmin)


class RedirectAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'regex', 'public', 'created_at', 'updated_at']
	search_fields = ['from_domain', 'from_url', 'to_domain', 'to_url', 'regex', 'public', 'created_at', 'updated_at']
	list_filter = ['from_domain', 'to_domain', 'public', 'regex']
	list_editable = ['public', 'regex']

admin.site.register(Redirect, RedirectAdmin)


class SiteSettingsAdmin(admin.ModelAdmin):
	list_display = ['site', 'language']
	search_fields = ['site', 'language']
	list_filter = ['site', 'language']


admin.site.register(SiteSettings, SiteSettingsAdmin)
