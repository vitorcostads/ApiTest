from django.db.models import fields
from rest_framework import serializers
from client.models import client
from rent.API.serializers import rentSerializers

class clientSerializers(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = "__all__"

class HistorySerializers(serializers.ModelSerializer):
    Rents = rentSerializers(many=True, read_only=True)


    class Meta:
        model = client
        fields = [
            'id_client',
            'CPF',
            'name',
            'birthday',
            'adress',
            'number_adress',
            'date',
            'Rents'
        ]