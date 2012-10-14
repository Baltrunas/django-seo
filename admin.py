# -*- coding: utf-8 -*
from django.contrib import admin
from seo.models import MetaData


class MetaDataAdmin(admin.ModelAdmin):
	list_display = ['title', 'header', 'url', 'public', 'created_at']
	search_fields = ['title', 'header', 'url', 'public', 'created_at']
	list_filter = ['public']
	list_editable = ['public']

	class Media:
		js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)

admin.site.register(MetaData, MetaDataAdmin)
