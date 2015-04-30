from .models import Data


def seo(request):
	try:
		seo_data = Data.objects.get(public=True, url=request.path_info, sites__id__in=[request.site.id])
	except:
		seo_data = False
	return {
		'seo': seo_data,
		'site': request.site,
		'url': request.url
	}
