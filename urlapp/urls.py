from django.urls import path

from .views import CreateShortUrl,redirect_short_url

urlpatterns = [
   path('api/shorten/',CreateShortUrl.as_view(),name = 'shorten-url'),
   path('<str:short_url_code>/',redirect_short_url,name='redirect-url')

]
