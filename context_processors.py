# -*- coding: utf-8 -*
from seo.models import Data


def seo(request):
	try:
		seo_data = Data.objects.get(public=True, url=request.path_info, sites__id=request.site.id)
	except:
		seo_data = False
	return {
		'seo': seo_data,
		'site': request.site,
		'url': request.url
	}