# -*- coding: utf-8 -*
from django import http
import re

from django.contrib.sites.models import Site
from seo import models as SEO

from django.middleware.locale import LocaleMiddleware
from django.utils import translation


from django.contrib.sites.shortcuts import get_current_site

# import os
# PROJECT_PATH = os.path.realpath(os.path.dirname(__file__) + '../')

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

		if request.is_secure():
			from_protocol = 'https://'
		else:
			from_protocol = 'http://'

		redirect_list = SEO.Redirect.objects.filter(from_domain=from_domain, from_protocol=from_protocol, public=True)

		for redirect in redirect_list:
			if redirect.regex:
				try:
					redirect_re = re.compile(redirect.from_url)
					if redirect_re.findall(from_url):
						to_url = re.sub(redirect.from_url, redirect.to_url, from_url)
						result_url = redirect.to_protocol + redirect.to_domain + to_url
						return http.HttpResponsePermanentRedirect(result_url)
				except:
					pass
			elif redirect.from_url == from_url:
				result_url = redirect.to_protocol + redirect.to_domain + redirect.to_url
				return http.HttpResponsePermanentRedirect(result_url)


class Host(object):
	def process_request(self, request):
		request.site = get_current_site(request)
		request.url = request.path_info


class SwitchLocale(LocaleMiddleware):
	def process_request(self, request):
		try:
			language = SEO.SiteSettings.objects.get(site=request.site).language
		except:
			language = LANGUAGE_CODE

		translation.activate(language)
		request.LANGUAGE_CODE = language


class SwitchTemplate(object):
	def process_request(self, request):
		site_settings = SEO.SiteSettings.objects.filter(site=request.site, public=True).first()

		if site_settings:
			settings.TEMPLATE_DIRS = (
				site_settings.template,
			) + settings.TEMPLATE_DIRS
