# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Functionality'
        db.create_table('domain_functionality', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('transdb.fields.TransCharField')(max_length=200)),
            ('description', self.gf('transdb.fields.TransCharField')(max_length=200)),
            ('path', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('accessExpression', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='functionalities', null=True, to=orm['domain.App'])),
        ))
        db.send_create_signal('domain', ['Functionality'])

        # Adding model 'Theme'
        db.create_table('domain_theme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('transdb.fields.TransCharField')(unique=True, max_length=200)),
            ('description', self.gf('transdb.fields.TransCharField')(max_length=200)),
            ('screenshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('domain', ['Theme'])

        # Adding model 'Host'
        db.create_table('domain_host', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('googleSearchEnabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('favicon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('supportEmailAddress', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('systemEmailAddress', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('copyright', self.gf('transdb.fields.TransCharField')(max_length=200)),
            ('title', self.gf('transdb.fields.TransCharField')(max_length=200)),
            ('subtitle', self.gf('transdb.fields.TransCharField')(max_length=200)),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['domain.Theme'])),
        ))
        db.send_create_signal('domain', ['Host'])

        # Adding model 'App'
        db.create_table('domain_app', (
            ('functionality_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['domain.Functionality'], unique=True, primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='apps', to=orm['domain.Host'])),
        ))
        db.send_create_signal('domain', ['App'])

        # Adding model 'MenuItem'
        db.create_table('domain_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('transdb.fields.TransCharField')(max_length=200)),
            ('description', self.gf('transdb.fields.TransCharField')(max_length=200)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['domain.Host'])),
            ('parentItem', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['domain.MenuItem'], null=True, blank=True)),
        ))
        db.send_create_signal('domain', ['MenuItem'])

        # Adding model 'MenuLink'
        db.create_table('domain_menulink', (
            ('menuitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['domain.MenuItem'], unique=True, primary_key=True)),
            ('functionality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['domain.Functionality'])),
        ))
        db.send_create_signal('domain', ['MenuLink'])

        # Adding model 'AppMenu'
        db.create_table('domain_appmenu', (
            ('menuitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['domain.MenuItem'], unique=True, primary_key=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['domain.App'])),
        ))
        db.send_create_signal('domain', ['AppMenu'])


    def backwards(self, orm):
        # Deleting model 'Functionality'
        db.delete_table('domain_functionality')

        # Deleting model 'Theme'
        db.delete_table('domain_theme')

        # Deleting model 'Host'
        db.delete_table('domain_host')

        # Deleting model 'App'
        db.delete_table('domain_app')

        # Deleting model 'MenuItem'
        db.delete_table('domain_menuitem')

        # Deleting model 'MenuLink'
        db.delete_table('domain_menulink')

        # Deleting model 'AppMenu'
        db.delete_table('domain_appmenu')


    models = {
        'domain.app': {
            'Meta': {'object_name': 'App', '_ormbases': ['domain.Functionality']},
            'functionality_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['domain.Functionality']", 'unique': 'True', 'primary_key': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'apps'", 'to': "orm['domain.Host']"})
        },
        'domain.appmenu': {
            'Meta': {'object_name': 'AppMenu', '_ormbases': ['domain.MenuItem']},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['domain.App']"}),
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
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['domain.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parentItem': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['domain.MenuItem']", 'null': 'True', 'blank': 'True'}),
            'title': ('transdb.fields.TransCharField', [], {'max_length': '200'})
        },
        'domain.menulink': {
            'Meta': {'object_name': 'MenuLink', '_ormbases': ['domain.MenuItem']},
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