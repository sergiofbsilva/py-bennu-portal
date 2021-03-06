from django.db import models
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
from transdb.fields import TransCharField

# Create your models here.

class Functionality(models.Model):
    title = TransCharField(max_length=200)
    description = TransCharField(max_length=200)
    path = models.CharField(max_length=1000)
    accessExpression = models.CharField(max_length=1000)
    application = models.ForeignKey('App', related_name = 'functionalities', null = True, blank = True)
    
    def __unicode__(self):
        return self.title

class Theme(models.Model):
    name = TransCharField(max_length=200, unique = True)
    description = TransCharField(max_length=200)
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
    copyright = TransCharField(max_length=200)
    title = TransCharField(max_length=200)
    subtitle = TransCharField(max_length=200)
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
    
    def uri(self):
      return "http://%s:%s/%s" % (self.hostname, "8080", "dot")
      
class App(Functionality):
    host = models.ForeignKey(Host, related_name="apps")
    
    def __unicode__(self):
        return "%s , %s" % (self.title, self.description) 
    
class MenuItem(models.Model):
    title = TransCharField(max_length=200)
    description = TransCharField(max_length=200)
    host = models.ForeignKey(Host, null = True, blank = True, default = None, related_name = "menu")
    parentItem = models.ForeignKey('self', null = True, blank = True, default = None, related_name = "child")
    
    def context_path(self):
      path = []
      if self.parentItem :
        path.append(self.parentItem)
      path.append(self)
      return path
    
    def __unicode__(self):
      return self.title
    
class MenuLink(MenuItem):
    functionality = models.ForeignKey(Functionality)
    appMenu = models.ForeignKey('AppMenu', related_name="links")
    
    def titlevalue(self):
      return self.title if self.title else self.functionality.title
    
    def descriptionvalue(self):
      return self.description if self.description else self.functionality.description
    
    def urlvalue(self):
      #return self.appMenu.app.host.uri() +  "/".join((self.appMenu.app.path , self.functionality.path))
      return self.appMenu.app.host.uri() + self.functionality.path
    
    def __unicode__(self):
        return "%s , %s" % (self.functionality.title, self.functionality.path)

class AppMenu(MenuItem):
    app = models.ForeignKey(App, related_name="menus")
    
    def __unicode__(self):
        return "%s , %s" % (self.title, self.description)
