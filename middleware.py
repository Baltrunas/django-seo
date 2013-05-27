# -*- coding: utf-8 -*
from django import http
import re

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
		from_domain = request.META.get('HTTP_HOST')
		from_url = request.path_info

		redirect_list = SEO.Redirect.objects.filter(from_domain=from_domain, public=True)

		if redirect_list:
			for redirect in redirect_list:
				if redirect.to_protocol:
					to_protocol = redirect.to_protocol
				else:
					to_protocol = 'http://'

				if redirect.regex:
					try:
						redirect_re = re.compile(redirect.from_url)
						if redirect_re.findall(from_url):
							to_url = re.sub(redirect.from_url, redirect.to_url, from_url)
							return http.HttpResponsePermanentRedirect(to_protocol + redirect.to_domain + to_url)
					except:
						pass
				elif redirect.from_url == from_url:
					return http.HttpResponsePermanentRedirect(to_protocol + redirect.to_domain + redirect.to_url)


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
