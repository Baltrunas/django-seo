# -*- coding: utf-8 -*
from django import http
from django.contrib.sites.models import Site
from seo import models as SEO

from django.middleware.locale import LocaleMiddleware
from django.utils import translation


from django.conf import settings

if hasattr(settings, 'SITE_ID'):
	SITE_ID = settings.SITE_ID
else:
	SITE_ID = 1

LANGUAGE_CODE = settings.LANGUAGE_CODE


class Redirect(object):
	def process_request(self, request):
		host = request.META.get('HTTP_HOST')

		if host == 'www.ronis.de':
			return http.HttpResponsePermanentRedirect('http://ronis.de' + request.path_info)

		if host:
			try:
				site = Site.objects.get(domain=host)
			except Site.DoesNotExist:
				site = Site.objects.get(pk=SITE_ID)

		redirect_list = SEO.Redirect.objects.filter(from_sites__id=site.id, from_url=request.path_info)
		if redirect_list:
			for redirect in redirect_list:
				if redirect.regex:
					pass
				else:
					return http.HttpResponsePermanentRedirect('http://' + redirect.to_site.domain + redirect.to_url)
		# 	if 'googlebot' in request.META['HTTP_USER_AGENT']:


class Host(object):
	def process_request(self, request):
		host = request.META.get('HTTP_HOST')
		if host:
			try:
				site = Site.objects.get(domain=host)
			except Site.DoesNotExist:
				site = Site.objects.get(pk=SITE_ID)
		request.site = site
		request.url = request.path_info


class SwitchLocale(LocaleMiddleware):
	def process_request(self, request):
		try:
			language = SEO.SiteSettings.objects.get(site=request.site).language
		except:
			language = LANGUAGE_CODE

		translation.activate(language)
		request.LANGUAGE_CODE = language
