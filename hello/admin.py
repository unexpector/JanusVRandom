from django.contrib import admin
from hello.models import Rooms, RandomSites, ObjectLibrary

class RandomSitesAdmin(admin.ModelAdmin):
    list_display = ('sitename', 'src')

# Register your models here.
admin.site.register(Rooms)
admin.site.register(RandomSites, RandomSitesAdmin)
admin.site.register(ObjectLibrary)

