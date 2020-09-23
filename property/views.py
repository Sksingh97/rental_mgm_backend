from master.models import PropertyType, LayoutType, FeatureType, RuleType, PriceRange
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from utils.responseHandler import sendSuccess, sendFailure
from master.serializers import PropertyTypeSerializer, LayoutTypeSerializer, FeatureTypeSerializer, RuleTypeSerializer, PriceRangeSerializer
import sys
from property.models import Property
from property.serializers import FileSerializer, PropertySerializer
from rest_framework.parsers import FileUploadParser
import ast
import urllib.parse



class FilterApi(APIView):
    """
    API to get filter valus for searching property or creating new property
    """

    def get(self, request):
        try:
            
            if 'type' in request.GET.keys():
                PropType_data = PropertyType.objects.filter(type=request.GET['type'],is_active=True)
                PropType = PropertyTypeSerializer(PropType_data, many=True).data
                LayType_data = LayoutType.objects.filter(type=request.GET['type'],is_active=True)
                LayType = LayoutTypeSerializer(LayType_data, many=True).data
                FeatType_data = FeatureType.objects.filter(type=request.GET['type'],is_active=True)
                FeatType = FeatureTypeSerializer(FeatType_data, many=True).data
                RuType_data = RuleType.objects.filter(type=request.GET['type'],is_active=True)
                RuType = RuleTypeSerializer(RuType_data, many=True).data
                PrRange_data = PriceRange.objects.filter(type=request.GET['type'])
                PrRange = PriceRangeSerializer(PrRange_data, many=True).data
                response_data={
                    'PropType':PropType,
                    'LayoutType':LayType,
                    'FeatureType':FeatType,
                    'RuleType':RuType,
                    'PriceRange':PrRange
                }
                return sendSuccess({"msg":"Filter data feched successfully","FilterData":response_data})
            else:
                return sendFailure("Type is required in order to fetch filter data")   
        except:
            print("ERRROR : : : :",sys.exc_info()[0])
            return sendFailure("Unable to fetch filter data")


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            
            return sendSuccess({"msg":"Image Uploaded Successfully","FileData":file_serializer.data})
        else:
            return sendFailure(file_serializer.errors)

class PropertyApi(APIView):
    """
    API to create property
    """

    def get(self, request):
        try:
            if request.GET['filter']:
                print(request.GET)

                # request.GET = urllib.parse.unquote(request.GET)
                print(request.GET)
                filter = {}
                keys = request.GET.keys()
                if 'no_bed_room' in keys:
                    filter['no_bed_room']=request.GET['no_bed_room']
                if 'no_bath_room' in keys:
                    filter['no_bath_room']=request.GET['no_bath_room']
                if 'approx_sqf' in keys:
                    filter['approx_sqf__gte'] = request.GET['approx_sqf']
                if 'prop_type' in keys:
                    filter['prop_type'] = request.GET['prop_type']
                if 'add_features' in keys:
                    print(type(ast.literal_eval(request.GET['add_features'])))
                    filter['add_features__overlap'] = ast.literal_eval(request.GET['add_features'])+['1']
                if 'rule' in keys:
                    filter['rule__overlap'] = ast.literal_eval(request.GET['rule']).append('test')+['2']
                if 'prop_details' in keys:
                    filter['prop_details__overlap'] = ast.literal_eval(request.GET['prop_details'])+['3']
            print(filter)
            property_data = Property.objects.filter(**filter).order_by('pk')
            serialized_data = PropertySerializer(property_data,many=True)
            return sendSuccess({"msg":"Property List Loaded Successfully","Property":serialized_data.data})
        except:
            print("ERRROR : : : :",sys.exc_info()[0])
            return sendFailure("Unable to fetch property")

    def post(self, request):
        # try:
        property_obj={
            'image_urls':ast.literal_eval(request.data['image_urls']),
            'no_bed_room':request.data['no_bed_room'],
            'no_bath_room':request.data['no_bath_room'],
            'address':request.data['address'],
            'city':request.data['city'],
            'state':request.data['state'],
            'zip_code':request.data['zip_code'],
            'country':request.data['country'],
            'approx_sqf':request.data['approx_sqf'],
            'per_month_rent':request.data['per_month_rent'],
            'nego':request.data['nego'],
            'prop_type':request.data['prop_type'],
            'add_features':ast.literal_eval(request.data['add_features']),
            'rule':ast.literal_eval(request.data['rule']),
            'prop_details':ast.literal_eval(request.data['prop_details']),
            'more_detail':request.data['more_detail'],
            'type':request.data['type'],
            'status':request.data['status']
        }
        print(property_obj)
        property_data = PropertySerializer(data=property_obj)
        if property_data.is_valid():
            property_data.save()
            return sendSuccess({"msg":"Property List Loaded Successfully","Property":property_data.data})
        else:
            print(property_data.errors)
            return sendFailure("Unable to create property")

        # except:
        #     print("ERRROR : : : :",sys.exc_info()[0])

        #     return sendFailure("Unable to create property")
