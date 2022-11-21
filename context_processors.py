from .models import Data


def seo(request):
    data = Data.objects.filter(public=True, url=request.path_info, site=request.site).first()
    return {"seo": data}
