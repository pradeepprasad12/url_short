from django.urls import path
from .views import CreateShortURL, redirect_short_url

urlpatterns = [
    path('api/shorten/', CreateShortURL.as_view(), name='shorten-url'),
    path('<str:short_code>/', redirect_short_url, name='redirect-url'),
]
