# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0003_auto_20160219_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='template',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Template', choices=[(b'/home/lesha/express-page/dev/apps/../templates/', b'templates')]),
        ),
    ]
