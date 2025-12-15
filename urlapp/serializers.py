from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = ['original_url', 'short_code', 'short_url']

    def get_short_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/{obj.short_code}/')
