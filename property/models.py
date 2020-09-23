from django.db import models
from django.contrib.postgres.fields import ArrayField

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name

class Property(models.Model):
    image_urls = ArrayField(models.CharField(max_length=255, blank=True))
    no_bed_room = models.IntegerField(default=1)
    no_bath_room = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    approx_sqf = models.FloatField(default=0.0)
    per_month_rent = models.IntegerField(default=0)
    nego = models.BooleanField(default=False)
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
    prop_type = models.CharField(max_length=255,null=True)
    add_features = ArrayField(models.CharField(max_length=255, blank=True))
    rule = ArrayField(models.CharField(max_length=255, blank=True))
    prop_details = ArrayField(models.CharField(max_length=255, blank=True))
    more_detail = models.CharField(max_length=1000,null=True)
    type = models.IntegerField(null=True)
    status = models.IntegerField(default=0)