# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class Data(models.Model):
	title = models.CharField(verbose_name=_('Title'), max_length=256)
	header = models.CharField(verbose_name=_('Header'), max_length=256)
	keywords = models.CharField(verbose_name=_('Keywords'), max_length=1024, blank=True, null=True)
	description = models.CharField(verbose_name=_('Description'), max_length=2048, blank=True, null=True)
	url = models.CharField(verbose_name=_('URL'), max_length=1024, editable=False)
	intro_text = models.TextField(verbose_name=_('Intro Text'), blank=True, null=True)
	text = models.TextField(verbose_name=_('Text'), blank=True, null=True)
	sites = models.ManyToManyField(Site, related_name='metadata', verbose_name=_('Sites'), null=True, blank=True)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def get_absolute_url(self):
		return self.url

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-created_at']
		verbose_name = _('Meta Data')
		verbose_name_plural = _('Meta Data')


class Tag(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	value = models.CharField(verbose_name=_('Info'), max_length=2048, blank=True)
	TYPE_CHOICES = (
		('meta', _('Meta')),
		('script', _('Script')),
		('link', _('Link')),
		('string', _('String')),
	)
	tag_type = models.CharField(verbose_name=_('Type'), max_length=64, choices=TYPE_CHOICES)
	data = models.ForeignKey(Data, verbose_name=_('Data'))

	def __unicode__(self):
		return self.name + ' = ' + self.value

	class Meta:
		ordering = ['name']
		verbose_name = _('Meta Tag')
		verbose_name_plural = _('Meta Tags')
