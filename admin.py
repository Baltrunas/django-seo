from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Data, Redirect, SiteSettings, ExtraSettings


class DataAdmin(admin.ModelAdmin):
	list_display = ['title', 'header', 'url', 'public', 'created_at']
	search_fields = ['title', 'header', 'url', 'public', 'created_at']
	list_filter = ['public', 'site']
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


class ExtraSettingsForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ExtraSettingsForm, self).__init__(*args, **kwargs)
		if 'instance' in kwargs and kwargs['instance']:
			if kwargs['instance'].type == 'string':
				self.fields['value'] = forms.CharField(label=_('Value (string or int)'), max_length=128, required=True)
			elif kwargs['instance'].type == 'text':
				self.fields['value'] = forms.CharField(label=_('Text'), widget=forms.Textarea, required=False)
		else:
			self.fields['value'] = forms.CharField(label=_('Value (string or int)'), max_length=128, required=False, help_text=_('Safe for edit'))
			self.fields['value'].widget.attrs['readonly'] = True

	class Meta:
		model = ExtraSettings
		fields = ['site', 'name', 'key', 'type', 'value']


class ExtraSettingsAdmin(admin.ModelAdmin): 
	list_display = ['name', 'site', 'type', 'key', 'get_value']
	search_fields = ['name', 'key', 'value']
	list_filter = ['type', 'site', 'key']

	form = ExtraSettingsForm

admin.site.register(ExtraSettings, ExtraSettingsAdmin)
