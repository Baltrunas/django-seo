# -*- coding: utf-8 -*
from django.contrib import admin
from seo.models import Data
from seo.models import Tag
from seo.models import Redirect


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
	list_display = ['from_sites_list', 'from_url', 'to_site', 'to_url', 'regex', 'public', 'created_at', 'updated_at']
	search_fields = ['from_sites', 'from_url', 'to_site', 'to_url', 'regex', 'public', 'created_at', 'updated_at']
	list_filter = ['public', 'regex']
	list_editable = ['public']

admin.site.register(Redirect, RedirectAdmin)
