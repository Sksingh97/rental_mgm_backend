from master.models import PropertyType, LayoutType, FeatureType, RuleType, PriceRange
from rest_framework import serializers


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'

class LayoutTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayoutType
        fields = '__all__'

class FeatureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureType
        fields = '__all__'

class RuleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleType
        fields = '__all__'

class PriceRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceRange
        fields = '__all__'
