from domain.models import Functionality, App, Theme, Host, MenuItem, MenuLink , AppMenu , CustomMenuItem
from django.contrib import admin

class FunctionalityInline(admin.StackedInline):
    model = Functionality
    
class AppAdmin(admin.ModelAdmin):
    inlines = [ 
               FunctionalityInline,  ]

admin.site.register(Functionality)
admin.site.register(App,AppAdmin)
admin.site.register(Theme)
admin.site.register(Host)
admin.site.register(MenuItem)
admin.site.register(MenuLink)
admin.site.register(AppMenu)
admin.site.register(CustomMenuItem)