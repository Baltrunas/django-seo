# django-seo
Simple SEO app for django.


Allows you:
* Setup meta data by absoulute puth-url
* Setup redirects with RegExp support
* Configure robots.txt
* Configure sitemap.xml
* Create extra site settings
* Switch site language by domain 

Django 2.2 to 4.1.3
Python 3.7 to 3.10

# Install
* Add to INSTALLED_APPS ```'apps.seo',```
* Add to TEMPLATE_CONTEXT_PROCESSORS ```'apps.seo.context_processors.seo',```
* Add to MIDDLEWARE_CLASSES
```python
'apps.seo.middleware.RedirectMiddleware', # For redirects
'apps.seo.middleware.SwitchLocaleMiddleware', # For multi-languages sites
```

* Add to urls.py ```path("", include("apps.seo.urls")),```

* Add this code in your template between ```&lt;head&gt; and &lt;/head&gt;```

```html
<title>{% firstof seo.title title %} &rarr; {{ request.site.name }}</title>
<meta name='keywords' content='{% firstof seo.keywords keywords %}'>
<meta name='description' content='{% firstof seo.description description %}'>
{{ seo.head|safe }}
```
* Add ```{{ seo.footer|safe }}``` to footer
* Add ```{{ seo.intro|safe }}``` before main content
* Add ```{{ seo.outro|safe }}``` after main content
* Add ```{{ site.settings.head|safe }}``` to **head** global settings for site
* Add ```{{ site.settings.footer|safe }}``` to **footer** global settings for site
* Migrate```python manage.py migrate seo```


# ToDo
* Update SwitchLocale from django2-cms
* 
* 
* Documentation
* PyPI
* Exptra meta data

# Thing about
* Language as model
* Site languages for multi languages sites
* Language changer type
* Add logic to redirects
* Add logic to template changer
