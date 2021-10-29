from rest_framework import  viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from client.API.serializers import clientSerializers
from client.API.serializers import HistorySerializers
from client.models import client

from rest_framework.permissions import IsAuthenticated

class clientViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = clientSerializers
    queryset =  client.objects.all()

    @action(detail=True, methods=['get'])

    def History(self, request, pk=None, *args, **kwargs):
        queryset = client.objects.filter(pk=pk)
        self.serializer_class = HistorySerializers
        serializer =  self.get_serializer(queryset, many=True)

        return Response(serializer.data)
        
