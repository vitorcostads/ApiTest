from rest_framework import serializers
from rent.models import rent

class rentSerializers(serializers.ModelSerializer):
    class Meta:
        model = rent
        fields = "__all__"
