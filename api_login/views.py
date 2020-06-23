from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LoginAPI(APIView):
    def get(self,request):
        return Response({"message":"LoginAPI"},status.HTTP_200_OK)

# Create your views here.
