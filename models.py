from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from django.conf import settings


class Data(models.Model):
	title = models.CharField(verbose_name=_('Title'), max_length=256)
	header = models.CharField(verbose_name=_('Header'), max_length=256)
	keywords = models.CharField(verbose_name=_('Keywords'), max_length=1024, blank=True, null=True)
	description = models.CharField(verbose_name=_('Description'), max_length=2048, blank=True, null=True)
	url = models.CharField(verbose_name=_('URL'), max_length=256)

	intro = models.TextField(verbose_name=_('Intro'), blank=True, null=True)
	outro = models.TextField(verbose_name=_('Outro'), blank=True, null=True)

	head_code = models.TextField(verbose_name=_('Head Code'), blank=True, null=True)
	footer_code = models.TextField(verbose_name=_('Footer Code'), blank=True, null=True)

	site = models.ForeignKey(Site, verbose_name=_('Site'), related_name='metadata')
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def get_absolute_url(self):
		return self.url

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-created_at']
		unique_together = ['site', 'url']
		verbose_name = _('Meta Data')
		verbose_name_plural = _('Meta Data')


class Redirect(models.Model):
	PROTOCOLS = (
		('http://', _('HTTP')),
		('https://', _('HTTPS')),
	)
	from_protocol = models.CharField(verbose_name=_('From Protocol'), max_length=32, choices=PROTOCOLS)
	from_domain = models.CharField(verbose_name=_('From Domain'), max_length=256, blank=True, null=True)
	from_url = models.CharField(verbose_name=_('From URL'), max_length=2048)

	to_protocol = models.CharField(verbose_name=_('To Protocol'), max_length=32, choices=PROTOCOLS)
	to_domain = models.CharField(verbose_name=_('To Domain'), max_length=256)
	to_url = models.CharField(verbose_name=_('To URL'), max_length=2048)

	regex = models.BooleanField(verbose_name=_('RegEx'), default=False)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return '%s%s/%s &rarr; %s%s/%s' % (self.from_protocol, self.from_domain, self.from_url, self.to_protocol, self.to_domain, self.to_url)
	__unicode__.allow_tags = True

	class Meta:
		verbose_name = _('Redirect')
		verbose_name_plural = _('Redirects')


class SiteSettings(models.Model):
	site = models.ForeignKey(Site, verbose_name=_('Site'), related_name='settings')
	language = models.CharField(verbose_name=_('Language'), max_length=32)

	# TODO: I think it's wrong
	if hasattr(settings, 'TEMPLATE_DIRS') and settings.TEMPLATE_DIRS:
		TEMPLATES = []
		for template_puth in settings.TEMPLATE_DIRS:
			template_parts = template_puth.split('/')
			if template_parts[-1]:
				template_name = template_parts[-1]
			else:
				template_name = template_parts[-2]
			TEMPLATES.append((template_puth, template_name))
	else:
		TEMPLATES = False

	template = models.CharField(verbose_name=_('Template'), max_length=128, choices=TEMPLATES, blank=True, null=True)

	robots = models.TextField(verbose_name=_('robots.txt'), blank=True, null=True)

	code_head = models.TextField(verbose_name=_('Head Code'), blank=True, null=True)
	code_footer = models.TextField(verbose_name=_('Footer Code'), blank=True, null=True)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __init__(self, *args, **kwargs):

		super(SiteSettings, self).__init__(*args, **kwargs)
		if hasattr(self, 'site'):
			for es in self.site.extra_settings.all():
				setattr(self.site, es.key, es.value)

	class Meta:
		verbose_name = _('Site Settings')
		verbose_name_plural = _('Sites Settings')

	def __unicode__(self):
		return u'%s &rarr; %s' % (self.site, self.language)
	__unicode__.allow_tags = True


class ExtraSettings(models.Model):
	site = models.ForeignKey(Site, verbose_name=_('Site'), related_name='extra_settings')
	name = models.CharField(_('Name'), max_length=128)
	key = models.CharField(_('Key'), max_length=128)
	TYPE = (
		('text', _('Text')),
		('string', _('String')),
		('int', _('Integer')),
		('double', _('Double')),
		('file', _('File')),
	)
	type = models.CharField(_('Type'), max_length=32, choices=TYPE)
	value = models.FileField(_('Value'), max_length=50000, null=True, blank=True)

	def get_value(self):
		if self.type == 'text':
			if self.value:
				short = '%s' % self.value
				return short[:200] + '...'
		else:
			return self.value

	def __unicode__(self):
		return self.name
