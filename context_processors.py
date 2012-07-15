# -*- coding: utf-8 -*
from seo.models import MetaData

def seo(request):
	return {
		'seo': MetaData.objects.filter(public=True, url=request.path_info),
		'site': request.site,
		'url': request.path_info
	}