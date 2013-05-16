# django-cms
Best SEO for django.

# Install
* Add to INSTALLED_APPS ```'seo',```
* Add to TEMPLATE_CONTEXT_PROCESSORS ```'seo.context_processors.seo',```
* Add to MIDDLEWARE_CLASSES

```'seo.middleware.Host',
'seo.middleware.Redirect',
'seo.middleware.SwitchLocale',
```

* Add to urls.py ```url(r'^robots.txt$', 'seo.views.robots', name='robots'),```

* Add this code in your template between &lt;head&gt; and &lt;/head&gt;

```html
<title>{% if seo.title %}{{ seo.title|safe }}{% else %}{{ title|safe }}{% endif %} &rarr; {{site.name}}</title>
<meta name='keywords' content='{% if seo.keywords %}{{ seo.keywords }}{% else %}{{ keywords }}{% endif %}'>
<meta name='description' content='{% if seo.description %}{{ seo.description }}{% else %}{{ description }}{% endif %}'>
{% for tag in seo.tags.all %}
	{{tag.display|safe}}
{% endfor %}
```

* Sync bata base ```./manage.py syncdb```


# Futures
* Redirects
	* Add logic
	* Add RegEx
* SitesGroups
* Aditional Meta Tags
	* Canonical
* Sitemap
* Add translations
* Add fixtures
* Documentation
* Improve
	* https://github.com/thisismess/django-seo-cascade
	* https://github.com/willhardy/django-seo
	* http://pypi.python.org/pypi/django-seo


# Changelog
## 2013.05.16
###Add
* Add Site Settings
* Add robots.txt (Allow to setup robots.txt in site settings)
* Add SwitchLocaleMiddleware (Allow to setup domain locale in site settings)
* Add .gitignore

### Fix
* README.md

## 2012.10.14
### Add
* Add Teg to template.
* Add Tag model.
* Add Redirect model.

### Fix
* Rename MetaData model to Data.
* Improve context_procesor
* Add fields to Redirect model.

## 2012.07.14
### Add
* MetaData model.

### Fix
* Move template context  processor to context_processors.py
* Optimized SEO template context  processor.

## 2012.07.13
* Now, SEO is a standalone application.