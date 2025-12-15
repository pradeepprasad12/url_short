

from rest_framework import serializers
from .models import shorturl

class shorturlserializers(serializers.ModelSerializer):
    short_url_code = serializers.SerializerMethodField()

    class Meta:
        model = shorturl
        fields = ['original_url','short_url','short_url_code']

    def get_short_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_url(f'/{obj.short_url}')
