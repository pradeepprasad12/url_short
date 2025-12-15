from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ShortURL
from .serializers import ShortURLSerializer


class CreateShortURL(APIView):
    def post(self, request):
        serializer = ShortURLSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            short_url = ShortURL.objects.create(
                original_url=serializer.validated_data['original_url']
            )
            return Response(
                ShortURLSerializer(short_url, context={'request': request}).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def redirect_short_url(request, short_code):
    url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(url.original_url)
