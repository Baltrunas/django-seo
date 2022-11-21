import re

from django.http import HttpResponsePermanentRedirect

from django.middleware.locale import LocaleMiddleware
from django.utils import translation
from django.conf import settings

from .models import Redirect


class RedirectMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from_domain = request.get_host()
        from_url = request.path_info

        if request.is_secure():
            from_protocol = "https://"
        else:
            from_protocol = "http://"

        redirect_list = Redirect.objects.filter(from_domain=from_domain, from_protocol=from_protocol, public=True)

        for redirect in redirect_list:
            if redirect.regex:
                try:
                    redirect_re = re.compile(redirect.from_url)
                    if redirect_re.findall(from_url):
                        to_url = re.sub(redirect.from_url, redirect.to_url, from_url)
                        result_url = redirect.to_protocol + redirect.to_domain + to_url
                        return HttpResponsePermanentRedirect(result_url)
                except:
                    pass
            elif redirect.from_url == from_url:
                result_url = redirect.to_protocol + redirect.to_domain + redirect.to_url
                return HttpResponsePermanentRedirect(result_url)

        return self.get_response(request)


class SwitchLocale(LocaleMiddleware):
    def process_request(self, request):
        if hasattr(request.site, "settings"):
            language = request.site.settings.language
        else:
            language = settings.LANGUAGE_CODE

        translation.activate(language)
        request.LANGUAGE_CODE = language
