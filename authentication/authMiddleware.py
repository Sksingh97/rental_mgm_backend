from authentication.serializers import UserSerializer
from authentication.models import MyUser
from utils.responseHandler import sendSuccess, sendFailure, sendFailureFromMidw
from django.http import HttpResponseForbidden 
from jose import jws
import json

class AuthMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        allowed_route_without_auth = ['/api/user/register','/api/user/otp','/api/user/login','/api/user/logout']
        print(request.path)
        if request.method == "POST":
            if request.path in allowed_route_without_auth:
                return self.get_response(request)
            else:
                request_body = self.get_request_data(request)
                token_data = self.get_token_data(request_body['token'])
                user_data = self.verify_user(token_data['id'])
                print("MIDDLEWARE : : : will be checked",user_data)
                # return sendFailure("Something went wrong")
                # return self.get_response(request)
                return sendFailureFromMidw("something went wrong")

        else:
            if request.path in allowed_route_without_auth:
                return self.get_response(request)
            else:
                # token_data = json.loads(jws.verify(request.data['token'], 'seKre8', algorithms=['HS256']))
                print("MIDDLEWARE : : : will be checked")
                return self.get_response(request)
    
    def get_request_data(self, request):
        if request.body:
            return json.loads(request.body)
        else:
            print("No Request Body")
            return False

    def get_token_data(self, token):
        token_data = json.loads(jws.verify(token, 'seKre8', algorithms=['HS256']))
        return token_data['user']

    def verify_user(self, id):
        try:
            user_data = MyUser.objects.get(pk=id)
            serialized_data = UserSerializer(user_data)
            return serialized_data.data
        except:
            return False
        
