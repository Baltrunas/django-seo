# -*- coding: utf-8 -*
from django.http import Http404
from django.conf import settings
from django import http
from django.contrib.sites.models import Site

class Redirect(object):
	def process_request(self, request):
		host = request.META.get('HTTP_HOST')
		if host:
			try:
				site = Site.objects.get(domain=host)
			except Site.DoesNotExist:
				site = Site.objects.get(pk=1)
			if host != site.domain:
				return http.HttpResponsePermanentRedirect('http://adeptgroup.ru' + request.path_info)

		office = Office.objects.get(sites__id=site.id)

		if office.main:
			if site.domain != 'adeptgroup.ru':
				return http.HttpResponsePermanentRedirect('http://adeptgroup.ru' + request.path_info)
		else:
			if 'googlebot' in request.META['HTTP_USER_AGENT']:
				if 'adeptgroup.ru' in site.domain:
					for rsite in office.sites.all():
						if 'xn--p1ai' in rsite.domain:
							return http.HttpResponsePermanentRedirect('http://' + rsite.domain + request.path_info)
			else:
				if 'xn--p1ai' in site.domain:
					for rsite in office.sites.all():
						if 'adeptgroup.ru' in rsite.domain:
							return http.HttpResponsePermanentRedirect('http://' + rsite.domain + request.path_info)

		# return response

class Host(object):
	def process_request(self, request):
		host = request.META.get('HTTP_HOST')
		if host:
			try:
				site = Site.objects.get(domain=host)
			except Site.DoesNotExist:
				site = Site.objects.get(pk=1)
		request.site = site
		request.url  = request.path_info
