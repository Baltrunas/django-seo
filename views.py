from django.template import RequestContext
from django.template import Template

from django.http import HttpResponse

from .models import SiteSettings


def robots(request):
	context = {}
	try:
		context['site_settings'] = SiteSettings.objects.get(site=request.site)
		robots_template = context['site_settings'].robots
	except:
		robots_template = ''

	tpl = Template(robots_template)

	context_instance = RequestContext(request)
	context_instance.update(context)

	html = tpl.render(context_instance)
	return HttpResponse(html, mimetype='text/plain')
