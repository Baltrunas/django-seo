from django.db import models
from django.contrib.sites.models import Site
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class Data(models.Model):
    site = models.ForeignKey(Site, verbose_name=_("Site"), related_name="metadata", on_delete=models.CASCADE)
    url = models.CharField(_("URL"), max_length=128)

    title = models.CharField(_("Title"), max_length=256)
    header = models.CharField(_("Header"), max_length=256)
    keywords = models.CharField(_("Keywords"), max_length=1024, blank=True, null=True)
    description = models.CharField(_("Description"), max_length=2048, blank=True, null=True)

    intro = models.TextField(_("Intro"), blank=True, null=True)
    outro = models.TextField(_("Outro"), blank=True, null=True)

    head = models.TextField(_("Extra head code"), blank=True, null=True)
    footer = models.TextField(_("Extra footer code"), blank=True, null=True)

    public = models.BooleanField(_("Public"), default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def get_absolute_url(self):
        return self.url

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["site", "url"]
        verbose_name = _("Meta data")
        verbose_name_plural = _("Meta data")


class Redirect(models.Model):
    PROTOCOLS = (
        ("http://", _("HTTP")),
        ("https://", _("HTTPS")),
    )
    from_protocol = models.CharField(verbose_name=_("From Protocol"), max_length=32, choices=PROTOCOLS)
    from_domain = models.CharField(verbose_name=_("From Domain"), max_length=256, blank=True, null=True)
    from_url = models.CharField(verbose_name=_("From URL"), max_length=2048)

    to_protocol = models.CharField(verbose_name=_("To Protocol"), max_length=32, choices=PROTOCOLS)
    to_domain = models.CharField(verbose_name=_("To Domain"), max_length=256)
    to_url = models.CharField(verbose_name=_("To URL"), max_length=2048)

    regex = models.BooleanField(verbose_name=_("RegEx"), default=False)

    public = models.BooleanField(verbose_name=_("Public"), default=True)
    created_at = models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated At"), auto_now=True)

    def __str__(self):
        return mark_safe(
            "%s%s/%s &rarr; %s%s/%s"
            % (self.from_protocol, self.from_domain, self.from_url, self.to_protocol, self.to_domain, self.to_url,)
        )

    class Meta:
        verbose_name = _("Redirect")
        verbose_name_plural = _("Redirects")


class SiteSettings(models.Model):
    site = models.OneToOneField(Site, verbose_name=_("Site"), related_name="settings", on_delete=models.CASCADE)
    language = models.CharField(_("Language"), max_length=5)

    robots_txt = models.TextField(_("robots.txt"), blank=True)
    sitemap_xml = models.TextField(_("sitemap.xml"), blank=True)

    head = models.TextField(_("Extra head code"), blank=True, null=True)
    footer = models.TextField(_("Extra footer code"), blank=True, null=True)

    public = models.BooleanField(_("Public"), default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __init__(self, *args, **kwargs):
        super(SiteSettings, self).__init__(*args, **kwargs)
        if hasattr(self, "site"):
            for es in self.site.extra_settings.all():
                setattr(self.site, es.key, es.value)
                setattr(self, es.key, es.value)

    class Meta:
        verbose_name = _("Site settings")
        verbose_name_plural = _("Sites settings")

    def __str__(self):
        return mark_safe("%s &rarr; %s" % (self.site, self.language))


class ExtraSettings(models.Model):
    site = models.ForeignKey(Site, verbose_name=_("Site"), related_name="extra_settings", on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=128)
    key = models.CharField(_("Key"), max_length=128)
    TYPE = (
        ("text", _("Text")),
        ("string", _("String")),
        ("int", _("Integer")),
        ("double", _("Double")),
        ("file", _("File")),
    )
    type = models.CharField(_("Type"), max_length=32, choices=TYPE)
    value = models.FileField(_("Value"), max_length=5000, null=True, blank=True)

    def get_value(self):
        if self.type == "text":
            if self.value:
                short = u"%s" % self.value
                return short[:200] + "..."
        else:
            return self.value

    def __str__(self):
        return self.name
