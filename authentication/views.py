from authentication.models import MyUser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from authentication.serializers import UserSerializer
from utils.email import account_created_mail
import sys
import random



class UserApiSignup(APIView):
    """
    User signup Api view to create new users
    """

    def get (self, request):
        model = MyUser.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post (self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                account_created_mail(serializer.data)
                return Response({"result":serializer.data, "status":status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
            else:
                # print()
                return Response({
                "success": False,
                "error": {
                "errorCode": 5,
                # "error":serializer.errors,
                "msg": "{} already exist".format(", ".join(serializer.errors.keys()))
                },
                "time": 1594456857182,
                "permission_updated": False
                }, status=status.HTTP_400_BAD_REQUEST)
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return Response({
                "success": False,
                "error": {
                "errorCode": 5,
                "msg": "Something Went Wrong"
                },
                "time": 1594456857182,
                "permission_updated": False
                }, status=status.HTTP_400_BAD_REQUEST)



class UserApiOtp(APIView):
    """
    User otp Api view to create new users
    """

    def get (self, request):
        try:
            print(request.GET["email"],request.GET["phone"])
            model = MyUser.objects.get(email=request.GET["email"], phone=request.GET["phone"])
            model.otp=random.randint(1000,9999)
            model.save()
            serializer = UserSerializer(model)
            account_created_mail(serializer.data)
            return Response({"result":{"msg":"Otp Send Successfully"}, "status":status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return Response({"msg":"Something Went Wrong"}, status=status.HTTP_400_BAD_REQUEST)

    def post (self, request):
        try:
            record = MyUser.objects.get(email=request.data["email"],phone=request.data["phone"],otp=request.data["otp"])
            print("Fetched Record : : ",record)
            if record:
                record.phone_verified = True
                record.save()
                result = UserSerializer(record)
                serializer = UserSerializer(record)
                return Response({"result":{"user":serializer.data,"msg":"User Verification success"}, "status":status.HTTP_200_OK, }, status=status.HTTP_201_CREATED)
            else:
                return Response({"msg":"Entered Otp Is Invalid."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return Response({"msg":"Something Went Wrong"}, status=status.HTTP_400_BAD_REQUEST)


        
            

class UserApiLogin(APIView):
    """
    User otp Api view to create new users
    """

    def post (self, request):
        try:
            record = MyUser.objects.get(email=request.data["email"],password=request.data["password"])
            print("Fetched Record : : ",record)
            if record:
                record.phone_verified = True
                record.save()
                result = UserSerializer(record)
                serializer = UserSerializer(record)
                return Response({"result":{"user":serializer.data,"msg":"User Verification success"}, "status":status.HTTP_200_OK, }, status=status.HTTP_201_CREATED)
            else:
                return Response({"msg":"Entered Otp Is Invalid."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            print("Error : :  : : :",sys.exc_info()[0])
            return Response({"msg":"Something Went Wrong"}, status=status.HTTP_400_BAD_REQUEST)
