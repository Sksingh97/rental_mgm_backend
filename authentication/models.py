from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
# Create your models here.
class MyUser(AbstractUser):
    username = None
    USERNAME_FIELD = 'userName'
    REQUIRED_FIELDS = []
    objects = UserManager()
    name = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    # country = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, null=True)
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
    social_id = models.CharField(max_length=255, unique=True, null=True)
    userName = models.CharField(max_length=255, unique=True, null=True)
    id_deleted = models.BooleanField(default=False)
    color = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        ordering = ['id']

class UserToken (models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, unique=True, null=True, default=None)
    token = models.CharField(max_length=555, blank=True, null=True)
    device_type = models.IntegerField(blank=True, null=True)