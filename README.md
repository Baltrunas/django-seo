# django-seo
Best SEO app for django. Allow to configure robots.txt, locale for domain, setup title, keywords, description, seo texts for all pages in admin panel.


# Install
* Add to INSTALLED_APPS ```'apps.seo',```
* Add to TEMPLATE_CONTEXT_PROCESSORS ```'apps.seo.context_processors.seo',```
* Add to MIDDLEWARE_CLASSES
```
'apps.seo.middleware.Host',
'apps.seo.middleware.Redirect',
'apps.seo.middleware.SwitchLocale',
'apps.seo.middleware.SwitchTemplate',
```
* Add to urls.py ```url(r'^robots.txt$', 'seo.views.robots', name='robots'),```
* Add this code in your template between &lt;head&gt; and &lt;/head&gt;
```html
<title>{% firstof seo.title title %} &rarr; {{ site.name }}</title>
<meta name='keywords' content='{% firstof seo.keywords keywords %}'>
<meta name='description' content='{% firstof seo.description description %}'>
{{ seo.head_code|safe }}
```
* Add ```{{ seo.head_code|safe }}``` to footer
* Add ```{{ seo.intro|safe }}``` before main content
* Add ```{{ seo.outro|safe }}``` after main content

* Sync bata base ```./manage.py syncdb```


# TODO
* PIP
* Documentation

* Template changer to pages

* SitesGroups

* Language as model
* Site languages for multi languages sites
* Language changer type

* Add logic to redirects
* Add logic to template changer

* Sitemap

# Improve
* https://github.com/thisismess/django-seo-cascade
* https://github.com/willhardy/django-seo
* http://pypi.python.org/pypi/django-seo
* http://pragmaticstartup.wordpress.com/2013/04/08/12-seo-tips-for-django/
