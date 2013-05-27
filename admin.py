# -*- coding: utf-8 -*
from django.contrib import admin
from seo.models import Data
from seo.models import Tag
from seo.models import Redirect
from seo.models import SiteSettings


class TagInline(admin.TabularInline):
	model = Tag
	extra = 0


class DataAdmin(admin.ModelAdmin):
	list_display = ['title', 'header', 'url', 'public', 'created_at']
	search_fields = ['title', 'header', 'url', 'public', 'created_at']
	list_filter = ['public', 'sites']
	list_editable = ['public']
	inlines = [TagInline]

admin.site.register(Data, DataAdmin)


class RedirectAdmin(admin.ModelAdmin):
	list_display = ['from_domain', 'from_url', 'to_domain', 'to_url', 'regex', 'public', 'created_at', 'updated_at']
	search_fields = ['from_domain', 'from_url', 'to_domain', 'to_url', 'regex', 'public', 'created_at', 'updated_at']
	list_filter = ['from_domain', 'to_domain', 'public', 'regex']
	list_editable = ['public', 'regex']

admin.site.register(Redirect, RedirectAdmin)


class SiteSettingsAdmin(admin.ModelAdmin):
	list_display = ['site', 'language']
	search_fields = ['site', 'language']
	list_filter = ['site', 'language']


admin.site.register(SiteSettings, SiteSettingsAdmin)
