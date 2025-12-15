from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import shorturl
from .serializers import shorturlserializers

class CreateShortUrl(APIView):
    def post(self,request):
        serializer = shorturlserializers(data= request.data,contex={'request':request})
        if serializer.is_valid():
            short_url = shorturl.objects.create(origianl_url=serializer.validated_data['original_url'])
            return Response(shorturlserializers(short_url,context={'request':request}).data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
def redirect_short_url(request,short_url_code):
    url = get_object_or_404(shorturl,short_url_code=short_url_code)