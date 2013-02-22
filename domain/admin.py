from domain.models import Functionality, App, Theme, Host, MenuItem, MenuLink , AppMenu
from django.contrib import admin

class FunctionalityInline(admin.StackedInline):
    model = Functionality
    
  
class AppAdmin(admin.ModelAdmin):
    inlines = [ FunctionalityInline ]

class AppInline(admin.TabularInline):
    model = App
    
class HostAdmin(admin.ModelAdmin):
    inlines = [ AppInline ]
    

    
admin.site.register(Functionality)
admin.site.register(App,AppAdmin)
admin.site.register(Theme)
admin.site.register(Host, HostAdmin)
admin.site.register(MenuItem)
admin.site.register(MenuLink)
admin.site.register(AppMenu)