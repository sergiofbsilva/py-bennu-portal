from django.db import models
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
from translatable.models import TranslatableModel, get_translation_model

# Create your models here.

class Functionality(TranslatableModel):
    path = models.URLField(max_length=1000, unique = True)
    accessExpression = models.CharField(max_length=1000)
    app = models.ForeignKey('App')
    
    def __unicode__(self):
        return self.title

class FunctionalityTranslation(get_translation_model(Functionality,"functionality")):
    title = models.CharField(max_length=200)
    
class Theme(models.Model):
    name = models.CharField(max_length=200, unique = True)
    description = models.CharField(max_length=200)
    screenshot = models.ImageField(verbose_name="Screenshot", upload_to="images/screenshots/")
    
    def __unicode__(self):
        return self.name
        

class Host(models.Model):
    hostname = models.CharField(max_length=200, unique = True)
    googleSearchEnabled = models.BooleanField()
    logo = models.ImageField(verbose_name="Logotipo", upload_to="images/logos/")
    favicon = models.ImageField(verbose_name="FavIcon", upload_to="images/favicons/")
    supportEmailAddress = models.CharField(max_length=200)
    systemEmailAddress = models.CharField(max_length=200)
    copyright = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme)
    
    def __unicode__(self):
        return self.hostname
    
    @classmethod
    def get_fields(cls):
        fields = []
        ignoredTypes = [AutoField, ForeignKey]
        for field in cls._meta.fields:
            if not type(field) in ignoredTypes:
                fields.append(field.name)
        return fields

class App(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    accessExpression = models.CharField(max_length=200)
    host = models.ForeignKey(Host)
    
    def __unicode__(self):
        return "%s , %s" % (self.title, self.description) 
    
class MenuItem(models.Model):
    host = models.ForeignKey(Host)
    parentItem = models.ForeignKey('self')
    
class MenuLink(MenuItem):
    functionality = models.ForeignKey(Functionality)
    
    def __unicode__(self):
        return "%s , %s" % (self.functionality.title, self.functionality.path)

class AppMenu(MenuItem):
    app = models.ForeignKey(App)
    
    def __unicode__(self):
        return self.app

class CustomMenuItem(MenuItem):
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title
