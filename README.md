# django-cms
SEO for django.

# Install
* Add 'seo', to INSTALLED_APPS
* ./manage.py syncdb
* TEMPLATE_CONTEXT_PROCESSORS 	'seo.context_processors.SEO',
* Add to MIDDLEWARE_CLASSES 'seo.middleware.Host',

# Futures
* Add Rederects middleware to MIDDLEWARE_CLASSES 'cms.middleware.Redirect',
* Add SitesGroups.
* Add Redirects.
* Add MetaTeg.

# Changelog
## 2012.07.14
### Add
* MetaData model.

### Fix
* Move template context  processor to context_processors.py
* Optimized SEO template context  processor.

## 2012.07.13
* Now, SEO is a standalone application.