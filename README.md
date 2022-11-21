# django-seo
Realy good SEO app for django. 

Allows you:
* Configure robots.txt
* Configure sitemap.xml
* Setup 301 redirects with RegExp support
* Setup meta data by absoulute puth-url
* Create extra settings
* Switch domain language

Last test on Django 4.1.3

# Install
* Add to INSTALLED_APPS ```'apps.seo',```
* Add to TEMPLATE_CONTEXT_PROCESSORS ```'apps.seo.context_processors.seo',```
* Add to MIDDLEWARE_CLASSES
```python
'apps.seo.middleware.RedirectMiddleware', # For redirects
'apps.seo.middleware.SwitchLocale', # For multi-languages sites
'apps.seo.middleware.SwitchTemplate', # For site with difference templates
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
* Rewrite SwitchLocale
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
