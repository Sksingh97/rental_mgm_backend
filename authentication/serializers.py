from authentication.models import MyUser, UserToken
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = '__all__'