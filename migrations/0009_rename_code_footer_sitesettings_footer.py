# Generated by Django 4.1.3 on 2022-11-21 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("seo", "0008_rename_code_head_sitesettings_head"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sitesettings", old_name="code_footer", new_name="footer",
        ),
    ]