"""rental_mgm_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authentication.views import UserApiSignup, UserApiOtp, UserApiLogin, UserDeviceToken, UserLogOut
from master.views import PropertyTypeApi, LayoutTypeApi, FeatureTypeApi, RuleTypeApi, PriceRangeApi
from rest_framework_simplejwt import views as jwt_views
router = routers.DefaultRouter()



urlpatterns = [
    path('api/user/register', UserApiSignup.as_view(), name="SignUp"),
    path('api/user/otp', UserApiOtp.as_view(), name="Otp"),
    path('api/user/login', UserApiLogin.as_view(), name="Login"),
    path('api/user/token', UserDeviceToken.as_view(), name="Token"),
    path('api/user/logout', UserLogOut.as_view(), name="Logout"),
    path('api/master/propertytype', PropertyTypeApi.as_view(), name="PropertyType"),
    path('api/master/layouttype', LayoutTypeApi.as_view(), name="LayoutType"),
    path('api/master/featuretype', FeatureTypeApi.as_view(), name="FeatureType"),
    path('api/master/ruletype', RuleTypeApi.as_view(), name="RuleType"),
    path('api/master/pricerange', PriceRangeApi.as_view(), name="PriceRange"),
    path('admin/', admin.site.urls),
]
