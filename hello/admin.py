from django.contrib import admin
from hello.models import Rooms, RandomSites, ObjectLibrary

# Register your models here.
admin.site.register(Rooms)
admin.site.register(RandomSites)
admin.site.register(ObjectLibrary)