from authentication.models import MyUser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from authentication.serializers import UserSerializer



class UserApiSignup(APIView):
    """
    User signup Api view to create new users
    """

    def get (self, request):
        return Response({"msg":"Welcome To Shelter Of Dream Please Signup"}, status=status.HTTP_200_OK)

    def post (self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserApiLogin(APIView):
    """
    User signup Api view to create new users
    """

    def get (self, request):
        return Response({"msg":"PLease provide email and password to login"}, status=status.HTTP_200_OK)

    def post (self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
