# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Rename 'Data.intro_text' field to 'Data.intro'
        db.rename_column('seo_data', 'intro_text', 'intro')

        # Rename 'Data.text' field to 'Data.outro'
        db.rename_column('seo_data', 'text', 'outro')


    def backwards(self, orm):
        # Rename 'Data.intro' field to 'Data.intro_text'
        db.rename_column('seo_data', 'intro', 'intro_text')

        # Rename 'Data.outro' field to 'Data.text'
        db.rename_column('seo_data', 'outro', 'text')


    models = {
        u'seo.data': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Data'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'footer_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'head_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'outro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'metadata'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'seo.redirect': {
            'Meta': {'object_name': 'Redirect'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_domain': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'from_protocol': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'from_url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'regex': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'to_domain': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'to_protocol': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'to_url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'seo.sitesettings': {
            'Meta': {'object_name': 'SiteSettings'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'robots': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'settings'", 'to': u"orm['sites.Site']"}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['seo']