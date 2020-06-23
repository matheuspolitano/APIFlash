from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DataAPI(APIView):
    def get(self,request):
        return Response({"message":"DataAPI"},status.HTTP_200_OK)

# Create your views here.
