from django.contrib import admin

# Register your models here.
from .models import Header, Sidebar, Project, Menu, Menu_item

admin.site.register(Project)
admin.site.register(Header)
admin.site.register(Sidebar)
admin.site.register(Menu)
admin.site.register(Menu_item)

