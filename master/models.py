from django.db import models


class PropertyType (models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    type = models.IntegerField(default=0,null=True)

class LayoutType (models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    type = models.IntegerField(default=0,null=True)

class FeatureType (models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    type = models.IntegerField(default=0,null=True)

class RuleType (models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    type = models.IntegerField(default=0,null=True)

class PriceRange (models.Model):
    min_value = models.IntegerField(default=0,null=True)
    max_value = models.IntegerField(default=0,null=True)
    type = models.IntegerField(default=0, unique=True)
