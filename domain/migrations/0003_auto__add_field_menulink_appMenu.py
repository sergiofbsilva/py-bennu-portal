# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MenuLink.appMenu'
        db.add_column('domain_menulink', 'appMenu',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='links', to=orm['domain.AppMenu']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MenuLink.appMenu'
        db.delete_column('domain_menulink', 'appMenu_id')


    models = {
        'domain.app': {
            'Meta': {'object_name': 'App', '_ormbases': ['domain.Functionality']},
            'functionality_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['domain.Functionality']", 'unique': 'True', 'primary_key': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'apps'", 'to': "orm['domain.Host']"})
        },
        'domain.appmenu': {
            'Meta': {'object_name': 'AppMenu', '_ormbases': ['domain.MenuItem']},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'menus'", 'to': "orm['domain.App']"}),
            'menuitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['domain.MenuItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        'domain.functionality': {
            'Meta': {'object_name': 'Functionality'},
            'accessExpression': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'functionalities'", 'null': 'True', 'to': "orm['domain.App']"}),
            'description': ('transdb.fields.TransCharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            'title': ('transdb.fields.TransCharField', [], {'max_length': '200'})
        },
        'domain.host': {
            'Meta': {'object_name': 'Host'},
            'copyright': ('transdb.fields.TransCharField', [], {'max_length': '200'}),
            'favicon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'googleSearchEnabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'subtitle': ('transdb.fields.TransCharField', [], {'max_length': '200'}),
            'supportEmailAddress': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'systemEmailAddress': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['domain.Theme']"}),
            'title': ('transdb.fields.TransCharField', [], {'max_length': '200'})
        },
        'domain.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'description': ('transdb.fields.TransCharField', [], {'max_length': '200'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['domain.Host']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parentItem': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'child'", 'null': 'True', 'blank': 'True', 'to': "orm['domain.MenuItem']"}),
            'title': ('transdb.fields.TransCharField', [], {'max_length': '200'})
        },
        'domain.menulink': {
            'Meta': {'object_name': 'MenuLink', '_ormbases': ['domain.MenuItem']},
            'appMenu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': "orm['domain.AppMenu']"}),
            'functionality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['domain.Functionality']"}),
            'menuitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['domain.MenuItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        'domain.theme': {
            'Meta': {'object_name': 'Theme'},
            'description': ('transdb.fields.TransCharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('transdb.fields.TransCharField', [], {'unique': 'True', 'max_length': '200'}),
            'screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['domain']