from django.db import models

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=128, unique=True)
    localasset = models.URLField()
    col = models.CharField(max_length=128)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class ObjectLibrary(models.Model):
    objectname = models.CharField(max_length=128, unique=True)
    idseed = models.CharField(max_length=128, unique=True)
    src = models.URLField()
    texsrc = models.URLField()

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.objectname

class RandomSites(models.Model):
    sitename = models.CharField(max_length=128, unique=True)
    src = models.URLField()

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.sitename

