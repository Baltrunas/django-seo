# -*- coding: utf-8 -*
from django import http
from django.contrib.sites.models import Site
from seo import models as SEO


class Redirect(object):
	def process_request(self, request):
		host = request.META.get('HTTP_HOST')
		if host:
			try:
				site = Site.objects.get(domain=host)
			except Site.DoesNotExist:
				site = Site.objects.get(pk=1)

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
				site = Site.objects.get(pk=1)
		request.site = site
		request.url = request.path_info
