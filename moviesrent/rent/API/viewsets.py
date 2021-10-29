from rest_framework import viewsets
from rent.API.serializers import rentSerializers
from rent.models import rent

from rest_framework.permissions import IsAuthenticated

class rentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = rentSerializers
    queryset =  rent.objects.all().order_by('recieve')
