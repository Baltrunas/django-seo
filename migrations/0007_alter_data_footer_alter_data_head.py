# Generated by Django 4.1.3 on 2022-11-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seo", "0006_rename_footer_code_data_footer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="footer",
            field=models.TextField(
                blank=True, null=True, verbose_name="Extra footer code"
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="head",
            field=models.TextField(
                blank=True, null=True, verbose_name="Extra head code"
            ),
        ),
    ]
