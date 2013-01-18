from django.core.management.base import NoArgsCommand
from domain.models import Host, AppMenu, MenuLink

class Command(NoArgsCommand):
  help = "Use this command to create the model from apps"

  def handle_noargs(self, **options):
    for host in Host.objects.all():
      print("processing host %s" % host.hostname)
      for app in host.apps.all():
        print("\tprocessing app %s" % app.title)
        appItem = AppMenu(app = app, title = app.title, description = app.description, parentItem = None, host = host)
        appItem.save()
        for functionality in app.functionalities.all():
          print("\t\tprocessing functionality %s" % functionality.path)
          menuLink = MenuLink(functionality = functionality, parentItem = appItem)
          menuLink.save()