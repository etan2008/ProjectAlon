# step 2: creating classes

#migrate every time you change something

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here

class BarangayBuoy(models.Model):
    province = models.CharField(max_length=220)
    municipality = models.CharField(max_length=220)
    barangay = models.CharField(max_length=220)
    buoy_number = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "Brgy {}, {}, {}; Buoy Number {}; LAT:{} LONG:{}".format(self.barangay,self.municipality,self.province,self.buoy_number,self.latitude,self.longitude)

class Intruder(models.Model):
    province = models.CharField(max_length=220)
    municipality = models.CharField(max_length=220)
    barangay = models.CharField(max_length=220)
    buoy_number = models.PositiveIntegerField()
    date = models.DateTimeField(default= timezone.now)
    recognized = models.BooleanField()

    def __str__(self):
        return "Intruder on Buoy Number {} of Brgy {}, {}, {}; Detected on {}".format(self.buoy_number,self.barangay,self.municipality,self.province,self.date)

class Fisherman(models.Model):
    province = models.CharField(max_length=220)
    municipality = models.CharField(max_length=220)
    barangay = models.CharField(max_length=220)
    id_number = models.CharField(max_length=220)
    name = models.CharField(max_length=220)
    date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return "Fisher {} of Brgy {}, {}, {}; ID Number {}; Registered on {} ".format(self.name, self.barangay, self.municipality, self.province, self.id_number, self.date)

class BuoyMessage(models.Model):
    province = models.CharField(max_length=220)
    municipality = models.CharField(max_length=220)
    barangay = models.CharField(max_length=220)
    buoy_number = models.PositiveIntegerField()
    id_number = models.CharField(max_length=220)
    date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return "Fisher {} of Brgy {}, {}, {}; ID Number {}; Registered on {} ".format(self.name, self.barangay, self.municipality, self.province, self.id_number, self.date)
