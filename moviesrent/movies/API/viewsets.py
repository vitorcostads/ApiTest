from rest_framework import viewsets
from movies.API.serializers import moviesSerializers
from movies.models import movies

from rest_framework.permissions import IsAuthenticated

class moviesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = moviesSerializers
    queryset =  movies.objects.all()
