# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class Data(models.Model):
	title = models.CharField(verbose_name=_('Title'), max_length=256)
	header = models.CharField(verbose_name=_('Header'), max_length=256)
	keywords = models.CharField(verbose_name=_('Keywords'), max_length=1024, blank=True, null=True)
	description = models.CharField(verbose_name=_('Description'), max_length=2048, blank=True, null=True)
	url = models.CharField(verbose_name=_('URL'), max_length=2048)
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
		('js', _('Java Script')),
		('css', _('CSS')),
		('string', _('String')),
	)
	tag_type = models.CharField(verbose_name=_('Type'), max_length=64, choices=TYPE_CHOICES)
	data = models.ForeignKey(Data, related_name='tags', verbose_name=_('Data'))
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def display(self):
		if self.tag_type == 'meta':
			return '<meta name="%s" content="%s">' % (self.name, self.value)
		if self.tag_type == 'css':
			return '<link rel="stylesheet" href="%s" type="text/css">' % (self.value)
		if self.tag_type == 'js':
			return '<script src="%s" type="text/javascript"></script>' % (self.value)
		if self.tag_type == 'string':
			return self.value
		else:
			return '<meta name="%s" content="%s">' % (self.name, self.value)

	def __unicode__(self):
		return self.name + ' = ' + self.value

	class Meta:
		ordering = ['name']
		verbose_name = _('Meta Tag')
		verbose_name_plural = _('Meta Tags')


class Redirect(models.Model):
	from_protocol = models.CharField(verbose_name=_('To Protocol'), max_length=32, blank=True, null=True, editable=False)
	from_domain = models.CharField(verbose_name=_('From Domain'), max_length=256, blank=True, null=True)
	from_url = models.CharField(verbose_name=_('From URL'), max_length=2048)

	to_protocol = models.CharField(verbose_name=_('To Protocol'), max_length=32, blank=True, null=True, editable=False)
	to_domain = models.CharField(verbose_name=_('To Domain'), max_length=256)
	to_url = models.CharField(verbose_name=_('To URL'), max_length=2048)

	regex = models.BooleanField(verbose_name=_('RegEx'), default=False)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return '%s%s &rarr; %s%s' % (self.from_domain, self.from_url, self.to_domain, self.to_url)
	__unicode__.allow_tags = True

	class Meta:
		verbose_name = _('Redirect')
		verbose_name_plural = _('Redirects')


class SiteSettings(models.Model):
	site = models.ForeignKey(Site, verbose_name=_('Site'), related_name='settings')
	language = models.CharField(verbose_name=_('Language'), max_length=32)

	robots = models.TextField(verbose_name=_('robots.txt'), blank=True, null=True)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	class Meta:
		verbose_name = _('Site Settings')
		verbose_name_plural = _('Sites Settings')

	def __unicode__(self):
		return '%s &rarr; %s' % (self.site, self.language)
	__unicode__.allow_tags = True
