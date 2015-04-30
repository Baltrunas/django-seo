from django.template import RequestContext
from django.template import Template

from django.http import HttpResponse


def robots(request):
	context = {}
	if hasattr(request.site, 'settings'):
		robots_template = request.site.settings.robots 
	else:
		robots_template = ''

	tpl = Template(robots_template)

	context_instance = RequestContext(request)
	context_instance.update(context)

	html = tpl.render(context_instance)
	return HttpResponse(html, content_type='text/plain')
