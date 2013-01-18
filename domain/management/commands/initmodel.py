from django.core.management.base import NoArgsCommand
from domain.models import Functionality, Host, Theme, App
from django.core.exceptions import ObjectDoesNotExist
import json

class Command(NoArgsCommand):
    help = "Use this command to initiliaze the database"

    def handle_noargs(self, **options):
        model = open('model.json', 'r').read()
        jsonmodel = json.loads(model)
        for host in jsonmodel['hosts']:
            hostname = host['hostname']
            try:
                hostmodel = Host.objects.get(hostname = hostname)
                print("host %s exists" % hostname)
            except ObjectDoesNotExist:
                print("host %s doesn't exists" % hostname)
                googleSearchEnabled = host['googleSearchEnabled']
                
                try:
                    logo = host['logo']
                except KeyError:
                    logo = ""
                    
                try:
                    favicon = jsonmodel['favicon']
                except KeyError:
                    favicon = ""
                     
                supportEmailAddress = host['supportEmailAddress']
                systemEmailAddress = host['systemEmailAddress']
                copyrightName = host['copyright']
                title = host['title']
                subtitle = host['subtitle']
                theme = self.createtheme(host['theme'])
                hostmodel = Host.objects.create(hostname = hostname, googleSearchEnabled = googleSearchEnabled, logo = logo, favicon = favicon, supportEmailAddress = supportEmailAddress, systemEmailAddress = systemEmailAddress, copyright = copyrightName , title = title, subtitle = subtitle, theme = theme)
                for app in host['apps']:
                    self.createapp(app, hostmodel)
                        
    def createtheme(self, jsontheme):
        name = jsontheme['name']
        try :
            theme = Theme.objects.get(name = name)
        except ObjectDoesNotExist:
            description = jsontheme['description']
            screenshot = jsontheme['screenshot']
            theme = Theme.objects.create(name = name , description = description, screenshot = screenshot)
        return theme
        
    def createapp(self, jsonapp, host):
        title = jsonapp['title']
        description = jsonapp['description']
        path = "/%s" % description['pt'].lower()
        accessExpression = jsonapp['accessExpression']
        app = App.objects.create(title = title, description = description, accessExpression = accessExpression, host = host, path = path)
        for functionality in jsonapp['functionalities']:
            self.createfunctionality(functionality, app)
        app.save();
        return app;
        
    def createfunctionality(self, jsonfunc, app):
        path = jsonfunc['path']
        try :
            func = Functionality.objects.get(path = path)
        except ObjectDoesNotExist:
            title = jsonfunc['title']
            accessExpression = jsonfunc['accessExpression']
            func = Functionality.objects.create(path = path, title = title, accessExpression = accessExpression, application = app)
        return func
