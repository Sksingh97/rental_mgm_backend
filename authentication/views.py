from authentication.models import MyUser, UserToken
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from authentication.serializers import UserSerializer, UserDeviceSerializer
from utils.email import account_created_mail
import sys
import random
from datetime import datetime
from google.oauth2 import id_token
from google.auth.transport import requests as grq
import requests
from utils.responseHandler import sendSuccess, sendFailure
from rest_framework_jwt.settings import api_settings
from jose import jws
import json

# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserApiSignup(APIView):
    """
    User signup Api view to create new users via normal creds or social
    """

    def get (self, request):
        model = MyUser.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post (self, request):
        print(request.data)
        if(request.data['sign_up_type'] == 0):
            try:
                request.data["otp"]=random.randint(1000,9999)
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    account_created_mail(serializer.data)
                    print("CREATED OBJ : : : ",serializer.data)
                    return sendSuccess({"user":serializer.data,"msg":"Sign Up Scessfully"})
                else:
                    # print()
                    return sendFailure("{} already exist".format(", ".join(serializer.errors.keys())))
            except:
                return sendFailure("Something Went Wrong")
        elif request.data['sign_up_type'] == 1:
            idinfo = id_token.verify_oauth2_token(request.data["token"], grq.Request(), '659153366205-2e9ir8g196l41idvfdu1k3mc0vs3o5o0.apps.googleusercontent.com')
            print(idinfo)
            request.data['profile_img'] = idinfo['picture']
            request.data['email_verified'] = True
            request.data['social_id'] = request.data['id']
            if idinfo['sub'] == request.data['id']:
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    print("CREATED OBJ : : : ",serializer.data)
                    token = jws.sign({"user":serializer.data}, 'seKre8',  algorithm='HS256')
                    return sendSuccess({"user":serializer.data,"msg":"Sign Up Scessfully","token":token})
                else:
                    return sendFailure("{} already exist".format(", ".join(serializer.errors.keys())))
            else:
                return sendFailure("Invalid Social Login Token")
        elif request.data['sign_up_type'] == 2:
            data = requests.get('https://graph.facebook.com/me?fields=name,email&access_token='+request.data['token'])
            print(data.json())
            request.data['name'] = data.json()['name']
            request.data['social_id'] = data.json()['id']
            if data.json()['id'] == request.data['id']:
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    # account_created_mail(serializer.data)
                    print("CREATED OBJ : : : ",serializer.data)
                    token = jws.sign({"user":serializer.data}, 'seKre8',  algorithm='HS256')
                    return sendSuccess({"user":serializer.data,"msg":"Sign Up Scessfully","token":token})
                else:
                    # print()
                    return sendFailure("{} already exist".format(", ".join(serializer.errors.keys())))
            else:
                return sendFailure("Invalid Social Login Token")
        else:
            return sendFailure("Invalid Request")



class UserApiOtp(APIView):
    """
    User otp Api view to verify user phone number and email
    """

    def get (self, request):
        try:
            print(request.GET["email"],request.GET["phone"])
            model = MyUser.objects.get(email=request.GET["email"], phone=request.GET["phone"])
            otp = random.randint(1000,9999)
            model.otp = otp
            model.save()
            serializer = UserSerializer(model)
            serializer.data.otp = otp
            print("SENDING OTP : : ",serializer)
            account_created_mail(serializer.data)
            return sendSuccess({"msg":"Otp Send Successfully"})
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return sendFailure("Something Went Wrong")

    def post (self, request):
        try:
            print("DATA : : : ",request.data)
            record = MyUser.objects.get(email=request.data["email"],phone=request.data["phone"],otp=request.data["otp"])
            # print("Fetched Record : : ",record)
            record.phone_verified = True
            record.otp = None
            record.otp_exp = None
            record.save()
            serializer = UserSerializer(record)
            serializer.data.pop('password')
            serializer.data.pop('otp')
            serializer.data.pop('otp_exp')
            token = jws.sign({"user":serializer.data}, 'seKre8',  algorithm='HS256')
            # print("TOKEN : : : :",token)
            return sendSuccess({"user":serializer.data,"msg":"Login Success","token":token})
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return sendFailure("Invalid Otp")


        
            

class UserApiLogin(APIView):
    """
    User login Api view to allow user to login using creds or social
    """

    def post (self, request):
        # print("@@@@@@@@@@@@@@::::",request.data)
        if request.data["log_in_type"] == 0:
            try:
                print(request.data)
                record = MyUser.objects.get(email=request.data["email"],password=request.data["password"])
                record.last_login = datetime.now()
                record.save()
                serializer = UserSerializer(record)
                token = jws.sign({"user":serializer.data}, 'seKre8',  algorithm='HS256')
                return sendSuccess({"user":serializer.data,"msg":"Login Success","token":token})
            except:
                return sendFailure("Invalid Credentials")
        elif request.data["log_in_type"] == 1:
            try:
                idinfo = id_token.verify_oauth2_token(request.data["token"], grq.Request(), '659153366205-2e9ir8g196l41idvfdu1k3mc0vs3o5o0.apps.googleusercontent.com')
                print(idinfo)
                record = MyUser.objects.get(email=idinfo['email'],social_id=idinfo['sub'])
                record.last_login = datetime.now()
                record.save()
                serializer = UserSerializer(record)
                token = jws.sign({"user":serializer.data}, 'seKre8',  algorithm='HS256')
                return sendSuccess({"user":serializer.data,"msg":"Login Success","token":token})
            except:
                print("Error : :  : : :",sys.exc_info()[0])
                return sendFailure("Account Doesn't Exist Please Sign Up 1")
        elif request.data["log_in_type"] == 2:
            try:
                data = requests.get('https://graph.facebook.com/me?fields=name,email&access_token='+request.data['token'])
                record = MyUser.objects.get(social_id=data.json()['id'])
                record.last_login = datetime.now()
                record.save()
                serializer = UserSerializer(record)
                token = jws.sign({"user":serializer.data}, 'seKre8',  algorithm='HS256')
                return sendSuccess({"user":serializer.data,"msg":"Login Success","token":token})
            except:
                return sendFailure("Account Doesn't Exist Please Sign Up First 2")
        else:
            return sendFailure("pdla la la ")



class UserDeviceToken(APIView):
    """
    User device token Api view to save fcm token of user for notifications
    """
    def post(self, request):
        print(request.data,request.user_profile)
        device_object = {
            "user_id":int(json.loads(request.user_profile)["id"]),
            "token":request.data['fcm_token'],
            "device_type":request.data['device_type']
        }
        try:
            record = UserToken.objects.get(user_id = device_object["user_id"])
            record.token = device_object["token"]
            record.save()
            serilized_data = UserDeviceSerializer(record)
            print("RECORD : : UPDATED : : ",serilized_data.data)
            return sendSuccess({"msg":"REGISTERING USER DEVICE"})
        except:
            print("ERROR : : : ",sys.exc_info()[0])
            record = UserDeviceSerializer(data=device_object)
            if record.is_valid():
                record.save()
                print("RECORD : : CREATED : : ",record.data)
                return sendSuccess({"msg":"REGISTERING USER DEVICE"})
            else:
                print("UNABLE TO SAVE RECORD : : :")
                return sendSuccess({})
            
            


class UserLogOut(APIView):
    """
    User logout Api view to logout user
    """

    def post(self, request):
        # print(request.data)
        # token_data = jws.decode(request.data['token'], 'seKre8', algorithms=['HS256'])
        # print(token_data)
        return sendSuccess({"msg":"REGISTERING USER DEVICE"})