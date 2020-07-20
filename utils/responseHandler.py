from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse


def sendSuccess(data):
    return Response({"result":data, "status":status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)

def sendFailure(msg):
    return Response({
                    "success": False,
                    "error": {
                    "errorCode": 5,
                    # "error":serializer.errors,
                    "msg": msg
                    },
                    "time": 1594456857182,
                    "permission_updated": False
                    }, status=status.HTTP_400_BAD_REQUEST)

def sendFailureFromMidw(msg):
    return JsonResponse({
                    "success": False,
                    "error": {
                    "errorCode": 5,
                    # "error":serializer.errors,
                    "msg": msg
                    },
                    "time": 1594456857182,
                    "permission_updated": False
                    }, status=status.HTTP_400_BAD_REQUEST)