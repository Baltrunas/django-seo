from django.http import HttpResponse, Http404


def robots_txt(request):
    if hasattr(request.site, "settings"):
        return HttpResponse(request.site.settings.robots_xml, content_type="text/xml")
    else:
        raise Http404


def sitemap_xml(request):
    if hasattr(request.site, "settings"):
        return HttpResponse(request.site.settings.sitemap_xml, content_type="text/xml")
    else:
        raise Http404
