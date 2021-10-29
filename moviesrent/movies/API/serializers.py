from rest_framework import serializers
from movies.models import movies

class moviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = movies
        fields = "__all__"

