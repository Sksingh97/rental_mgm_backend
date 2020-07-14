from django.db import models

# Create your models here.
class MyUser (models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    # country = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    dob = models.CharField(max_length=255, blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    otp_exp = models.DateTimeField(auto_now=True, blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    profile_img = models.CharField(max_length=255, blank=True, null=True)
    notification = models.BooleanField(default=True)
    phone_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)