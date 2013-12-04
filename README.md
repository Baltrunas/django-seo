# django-seo
Best SEO for django. Allow to configure robots.txt, locale for domain, setup title, keywords, description, seo texts for all pages in admin panel.


# Install
* Add to INSTALLED_APPS ```'seo',```
* Add to TEMPLATE_CONTEXT_PROCESSORS ```'seo.context_processors.seo',```
* Add to MIDDLEWARE_CLASSES
```
'seo.middleware.Host',
'seo.middleware.Redirect',
'seo.middleware.SwitchLocale',
```
* Add to urls.py ```url(r'^robots.txt$', 'seo.views.robots', name='robots'),```
* Add this code in your template between &lt;head&gt; and &lt;/head&gt;
```html
<title>{% firstof seo.title title %} &rarr; {{site.name}}</title>
<meta name='keywords' content='{% firstof seo.keywords keywords %}'>
<meta name='description' content='{% firstof seo.description description %}'>
```
* Sync bata base ```./manage.py syncdb```


# TODO
* Add head code block
* Language as model
* Site languages for multi languages
* Change title variables on fly
* Add logic to redirects
* SitesGroups
* Sitemap
* Add translations
* Template changer to pages
* Documentation
* Improve
	* https://github.com/thisismess/django-seo-cascade
	* https://github.com/willhardy/django-seo
	* http://pypi.python.org/pypi/django-seo
	* http://pragmaticstartup.wordpress.com/2013/04/08/12-seo-tips-for-django/

# Changelog
## 2013.12.04
* Delete Tags model
* Add redirects protocol
* New clear head code

## 2013.05.24
### Add
* Redirects
	* Add RegEx

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