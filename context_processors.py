from .models import Data


def seo(request):
    try:
        seo_data = Data.objects.get(public=True, url=request.path_info, site=request.site)
    except:
        seo_data = False
    return {
        "seo": seo_data,
    }
