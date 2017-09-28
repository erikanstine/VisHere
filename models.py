# from __future__ import unicode_literals
from django.db import models

class Building(models.Model):
    bldg_id = models.IntegerField(primary_key = True)
    BBL = models.IntegerField()
    BIN = models.IntegerField(default = 9999999)
    dateBuilt = models.IntegerField()
    roofHeight = models.FloatField()
    groundElevation = models.IntegerField()

    numFloors = models.FloatField()
    centerLat = models.FloatField()
    centerLon = models.FloatField()
    streetAddress = models.CharField(max_length=200, default = 'N/A')

    def __str__(self):
        return str(self.BIN) + ' - ' + self.streetAddress

class FullBuilding(models.Model):
    bldg_id = models.IntegerField(primary_key=True)
    bbl = models.IntegerField()
    bin = models.IntegerField()
    datebuilt = models.IntegerField()
    roofheight = models.FloatField()
    groundelevation = models.FloatField()
    numfloors = models.FloatField()
    centerlat = models.FloatField()
    centerlon = models.FloatField()
    streetaddress = models.CharField(max_length=200)


    def __str__(self):
        return str(self.bin) + ' - ' + self.streetaddress
