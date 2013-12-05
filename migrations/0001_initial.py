# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Data'
        db.create_table(u'seo_data', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('intro_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'seo', ['Data'])

        # Adding M2M table for field sites on 'Data'
        m2m_table_name = db.shorten_name(u'seo_data_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('data', models.ForeignKey(orm[u'seo.data'], null=False)),
            ('site', models.ForeignKey(orm[u'sites.site'], null=False))
        ))
        db.create_unique(m2m_table_name, ['data_id', 'site_id'])

        # Adding model 'Redirect'
        db.create_table(u'seo_redirect', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_protocol', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('from_domain', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('from_url', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('to_protocol', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('to_domain', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('to_url', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('regex', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'seo', ['Redirect'])

        # Adding model 'SiteSettings'
        db.create_table(u'seo_sitesettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='settings', to=orm['sites.Site'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('robots', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'seo', ['SiteSettings'])


    def backwards(self, orm):
        # Deleting model 'Data'
        db.delete_table(u'seo_data')

        # Removing M2M table for field sites on 'Data'
        db.delete_table(db.shorten_name(u'seo_data_sites'))

        # Deleting model 'Redirect'
        db.delete_table(u'seo_redirect')

        # Deleting model 'SiteSettings'
        db.delete_table(u'seo_sitesettings')


    models = {
        u'seo.data': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Data'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'metadata'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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