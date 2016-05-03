# django-seo
Realy good SEO app for django. 

Allows you:
* Configure robots.txt
* Setup 301 redirects with RegExp support
* Setup meta data by absoulute puth-url
* Create extra settings
* Switch domain language
* Switch domain template

Last test on Django 1.9.4, but I thitk in will work prety well on all major versions.

<!-- # Requeremnts -->
<!-- ```pip install django-helpfull``` -->

# Install
* Add to INSTALLED_APPS ```'apps.seo',```
* Add to TEMPLATE_CONTEXT_PROCESSORS ```'apps.seo.context_processors.seo',```
* Add to MIDDLEWARE_CLASSES
```python
'apps.seo.middleware.Host', # Don't use SITE_ID with it
'apps.seo.middleware.Redirect', # For redirects
'apps.seo.middleware.SwitchLocale', # For multilanguages sites
'apps.seo.middleware.SwitchTemplate', # For site with difference templates
```

* Add to urls.py ```url(r'^', include('apps.seo.urls')),```

* Add this code in your template between ```&lt;head&gt; and &lt;/head&gt;```

```html
<title>{% firstof seo.title title %} &rarr; {{ site.name }}</title>
<meta name='keywords' content='{% firstof seo.keywords keywords %}'>
<meta name='description' content='{% firstof seo.description description %}'>
{{ seo.head_code|safe }}
```
* Add ```{{ seo.footer_code|safe }}``` to footer
* Add ```{{ seo.intro|safe }}``` before main content
* Add ```{{ seo.outro|safe }}``` after main content
* Add ```{{ site.settings.code_head|safe }}``` to **head** global settings for site
* Add ```{{ site.settings.code_footer|safe }}``` to **footer** global settings for site
* Migrate```python manage.py migrate seo```


# ToDo
* Sitemap
* Documentation
* PyPI
* Exptra meta data

# Thing about
* Language as model
* Site languages for multi languages sites
* Language changer type
* Add logic to redirects
* Add logic to template changer

# May be added to SiteSettings model as part of django-lp

```python
title = models.CharField(verbose_name=_('Title'), max_length=128)
email = models.EmailField(max_length=128, verbose_name=_('E-Mail'))
send_email = models.BooleanField(verbose_name=_('Send E-Mail'), default=True)
phone = models.CharField(max_length=32, verbose_name=_('Phone'))
send_sms = models.BooleanField(verbose_name=_('Send SMS'), default=True)
sms_key = models.CharField(verbose_name=_('SMS.RU Key'), max_length=64, blank=True, null=True)
sms_name = models.CharField(verbose_name=_('SMS Name'), help_text=_('From 2 to 11 Latin characters.'), max_length=11)
```



<!-- 


Widgets
	Widgets handling input of text
		TextInput
		NumberInput
		EmailInput
		URLInput
		PasswordInput
		HiddenInput
		DateInput
		DateTimeInput
		TimeInput
		Textarea

	Selector and checkbox widgets
		CheckboxInput
		Select
		NullBooleanSelect
		SelectMultiple
		RadioSelect
		CheckboxSelectMultiple

	File upload widgets
		FileInput
		ClearableFileInput

	Composite widgets
		MultipleHiddenInput
		SplitDateTimeWidget
		SplitHiddenDateTimeWidget
		SelectDateWidget


Built-in Field classes
	- BooleanField
	+ CharField
	+\- ChoiceField
	- TypedChoiceField
	+ DateField
	+ DateTimeField
	+ DecimalField
	+ DurationField
	+ EmailField
	+ FileField
	+ FilePathField
	+ FloatField
	+ ImageField
	+ IntegerField
	+ GenericIPAddressField
	- MultipleChoiceField
	- TypedMultipleChoiceField
	- NullBooleanField
	+ RegexField
	+ SlugField
	+ TimeField
	+ URLField
	+ UUIDField



-->