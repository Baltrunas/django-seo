from django.template import RequestContext
from django.template import Template

from django.http import HttpResponse


def robots(request):
	if hasattr(request.site, 'settings'):
		robots_template = request.site.settings.robots 
	else:
		robots_template = ''

	tpl = Template(robots_template)

	html = tpl.render(RequestContext(request))
	return HttpResponse(html, content_type='text/plain')
