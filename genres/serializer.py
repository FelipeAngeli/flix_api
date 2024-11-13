from rest_framework import serializers
from genres.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre # model que será serializado
        fields = '__all__' # campos que serão serializados