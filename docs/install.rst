Install
=======

.. _django-seo: https://github.com/Baltrunas/django-seo
.. _GitHub: https://github.com/Baltrunas/django-seo

Download
--------

You can download django-seo_ from my GitHub_ repository.


Setup
-----

* Add to INSTALLED_APPS ``'seo',``
* Add to TEMPLATE_CONTEXT_PROCESSORS ``'seo.context_processors.seo',``
* Add to MIDDLEWARE_CLASSES

.. code-block:: python

	'seo.middleware.RedirectMiddleware',
	'seo.middleware.SwitchLocaleMiddleware',

* Add to urls.py ``path("", include("apps.seo.urls")),``
* Add this code in your template between <head> and </head>

.. code-block:: html

	<title>{% firstof seo.title title %} &rarr; {{ request.site.name }}</title>
	<meta name='keywords' content='{% firstof seo.keywords keywords %}'>
	<meta name='description' content='{% firstof seo.description description %}'>
	{{ seo.head|safe }}

* Add ``{{ seo.footer|safe }}`` to footer
* Add ``{{ seo.intro|safe }}`` before main content
* Add ``{{ seo.outro|safe }}`` after main content

* Migrate bata base ``./manage.py migrate seo``
