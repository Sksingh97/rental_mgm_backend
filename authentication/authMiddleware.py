from authentication.serializers import UserSerializer
from authentication.models import MyUser
from utils.responseHandler import sendSuccess, sendFailure, sendFailureFromMidw
from django.http import HttpResponseForbidden 
from jose import jws
import json
from rental_mgm_backend.message import get_message_by_key

class AuthMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        allowed_route_without_auth = ['/api/user/register','/api/user/otp','/api/user/login','/api/user/logout']
        # print(request.path,request.user,dir(request))
        request.POST = request.POST.copy()
        if request.method == "POST":

            if request.path in allowed_route_without_auth:
                print("ALLOWED URL")
                return self.get_response(request)
            else: 
                request_body = self.get_request_data(request)
                if 'Authorization' in request_body.keys():
                    token_data = self.get_token_data(request_body['Authorization'])
                    print("DATA : :  :",token_data)
                    user_data = self.verify_user(token_data['id'])
                    if not user_data:
                        return sendFailureFromMidw(get_message_by_key("Invalid Authorization token","en"))

                    # print("MIDDLEWARE : : : will be checked",user_data)
                    if user_data and user_data['id_deleted']:
                        return sendFailureFromMidw(get_message_by_key("AccountDeleted","en"))
                    if not user_data['is_active']:
                        return sendFailureFromMidw(get_message_by_key("AccountDeactivated","en"))
                    
                    request.user_profile = json.dumps({"id":user_data["id"]})

                    return self.get_response(request)
                else:
                    return sendFailureFromMidw(get_message_by_key("Un-authorized","en"))

        else:
            if request.path in allowed_route_without_auth:
                return self.get_response(request)
            else:
                print("MIDDLEWARE : : : will be checked")
                return self.get_response(request)
    
    def get_request_data(self, request):
        print("HEADERS : : :: ",request.headers)
        if request.headers:
            return request.headers
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
        
