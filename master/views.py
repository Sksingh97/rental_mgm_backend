from master.models import PropertyType, LayoutType, FeatureType, RuleType, PriceRange
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from utils.responseHandler import sendSuccess, sendFailure
from master.serializers import PropertyTypeSerializer, LayoutTypeSerializer, FeatureTypeSerializer, RuleTypeSerializer, PriceRangeSerializer
import sys

# Create your views here.



class PropertyTypeApi(APIView):
    """
    Property Type Api to add, update, delete types of property
    """

    def get (self, request):
        print(request.GET)
        property_type_data = PropertyType.objects.filter(type=request.GET['type'], is_active=True)
        property_data = PropertyTypeSerializer(property_type_data, many=True)
        return sendSuccess({"msg":"Get request PropertyTypeApi", "PropType":property_data.data})

    def put (self, request):
        try:
            print(request.data)
            property_data = PropertyType.objects.get(id=request.data['id'])
            property_data.name = request.data['name']
            property_data.is_active = request.data['is_active']
            property_data.type = request.data['type']
            property_data.save()
            response_data = PropertyTypeSerializer(property_data)
            return sendSuccess({"msg":"Property type updated","PropType":response_data.data})
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return sendFailure("Unable to find property type to edit")



    def post (self, request):
        print(request.data)
        property_type_data = PropertyTypeSerializer(data=request.data)
        if property_type_data.is_valid():
            property_type_data.is_active = True
            property_type_data.save()
            return sendSuccess({"msg":"Property Type Created", "PropType":property_type_data.data})
        else:
            return sendFailure("Unable to create property type")



class LayoutTypeApi(APIView):
    """
    Property Type Api to add, update, delete types of layout
    """

    def get (self, request):
        print(request.GET)
        layout_type_data = LayoutType.objects.filter(type=request.GET['type'], is_active=True)
        layout_data = LayoutTypeSerializer(layout_type_data, many=True)
        return sendSuccess({"msg":"Layout Type Fetched Successfully", "LayoutType":layout_data.data})

    def put (self, request):
        try:
            print(request.data)
            layout_data = LayoutType.objects.get(id=request.data['id'])
            layout_data.name = request.data['name']
            layout_data.is_active = request.data['is_active']
            layout_data.type = request.data['type']
            layout_data.save()
            response_data = LayoutTypeSerializer(layout_data)
            return sendSuccess({"msg":"Layout type updated","LayoutType":response_data.data})
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return sendFailure("Unable to find layout type to edit")



    def post (self, request):
        print(request.data)
        layout_type_data = LayoutTypeSerializer(data=request.data)
        if layout_type_data.is_valid():
            layout_type_data.is_active = True
            layout_type_data.save()
            return sendSuccess({"msg":"Layout Type Created", "LayoutType":layout_type_data.data})
        else:
            return sendFailure("Unable to create layout type")


class FeatureTypeApi(APIView):
    """
    Property Type Api to add, update, delete types of layout
    """

    def get (self, request):
        print(request.GET)
        feature_type_data = FeatureType.objects.filter(type=request.GET['type'], is_active=True)
        feature_data = FeatureTypeSerializer(feature_type_data, many=True)
        return sendSuccess({"msg":"Feature Type Fetched Successfully", "FeatureType":feature_data.data})

    def put (self, request):
        try:
            print(request.data)
            feature_data = FeatureType.objects.get(id=request.data['id'])
            feature_data.name = request.data['name']
            feature_data.is_active = request.data['is_active']
            feature_data.type = request.data['type']
            feature_data.save()
            response_data = FeatureTypeSerializer(feature_data)
            return sendSuccess({"msg":"Feature type updated","FeatureType":response_data.data})
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return sendFailure("Unable to find feature type to edit")


    def post (self, request):
        print(request.data)
        feature_type_data = FeatureTypeSerializer(data=request.data)
        if feature_type_data.is_valid():
            feature_type_data.is_active = True
            feature_type_data.save()
            return sendSuccess({"msg":"Feature Type Created", "FeatureType":feature_type_data.data})
        else:
            return sendFailure("Unable to create feature type")

class RuleTypeApi(APIView):
    """
    Property Type Api to add, update, delete types of rules
    """

    def get (self, request):
        print(request.GET)
        rule_type_data = RuleType.objects.filter(type=request.GET['type'], is_active=True)
        rule_data = RuleTypeSerializer(rule_type_data, many=True)
        return sendSuccess({"msg":"Rule Type Fetched Successfully", "RuleType":rule_data.data})

    def put (self, request):
        try:
            print(request.data)
            rule_data = RuleType.objects.get(id=request.data['id'])
            rule_data.name = request.data['name']
            rule_data.is_active = request.data['is_active']
            rule_data.type = request.data['type']
            rule_data.save()
            response_data = RuleTypeSerializer(rule_data)
            return sendSuccess({"msg":"Rule type updated","RuleType":response_data.data})
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return sendFailure("Unable to find rule type to edit")


    def post (self, request):
        print(request.data)
        rule_type_data = RuleTypeSerializer(data=request.data)
        if rule_type_data.is_valid():
            rule_type_data.is_active = True
            rule_type_data.save()
            return sendSuccess({"msg":"Rule Type Created", "RuleType":rule_type_data.data})
        else:
            return sendFailure("Unable to create rule type")


class PriceRangeApi(APIView):
    """
    Property Type Api to add, update, delete types of price range
    """

    def get (self, request):
        print(request.GET)
        price_range_data = PriceRange.objects.filter(type=request.GET['type'])
        price_range = PriceRangeSerializer(price_range_data, many=True)
        return sendSuccess({"msg":"Price Range Fetched Successfully", "PriceRange":price_range.data})

    def put (self, request):
        try:
            print(request.data)
            price_range = PriceRange.objects.get(type=request.data['type'])
            price_range.min_value = request.data['min_value']
            price_range.max_value = request.data['max_value']
            # price_range.type = request.data['type']
            price_range.save()
            response_data = PriceRangeSerializer(price_range)
            return sendSuccess({"msg":"Price Range updated","PriceRange":response_data.data})
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return sendFailure("Unable to find price range to edit")


    def post (self, request):
        print(request.data)
        price_range_data = PriceRangeSerializer(data=request.data)
        if price_range_data.is_valid():
            price_range_data.save()
            return sendSuccess({"msg":"Price Range Created", "PriceRange":price_range_data.data})
        else:
            print("ERROR : : : : : ::  :",price_range_data.errors.keys())
            return sendFailure("Unable to create price range")
