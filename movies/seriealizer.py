from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):
    #aqui add mais um campo no serializer para calcular a média de avaliações
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    #aqui implemento o método para calcular a média de avaliações
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
     



    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser menor que 1900')
        return value
    
    def validate_resume(self, value):
        if not (10 <= len(value) <= 200):
            raise serializers.ValidationError('O resumo deve ter entre 10 e 200 caracteres.')
        return value