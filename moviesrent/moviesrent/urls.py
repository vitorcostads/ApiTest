from django import urls
from django.contrib import admin
from django.urls import path, include
import rest_framework

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from movies.API.viewsets import moviesViewSet
from client.API.viewsets import clientViewSet
from rent.API.viewsets import rentViewSet

route = routers.DefaultRouter()
route.register(r'movies', moviesViewSet, basename= 'Movies')
route.register(r'client', clientViewSet, basename = 'Client' )
route.register(r'rent', rentViewSet, basename = 'Rent' )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(route.urls)),
    path('', include(route.urls)) 

]

