from django.db.models import Avg
from rest_framework import serializers
from actors.serializer import ActorSerializer
from genres.serializer import GenereSerializer
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser menor que 1900')
        return value

    def validate_resume(self, value):
        if not (10 <= len(value) <= 200):
            raise serializers.ValidationError('O resumo deve ter entre 10 e 200 caracteres.')
        return value


class MovieDetailSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(many=True)
    genre = GenereSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField(child=serializers.DictField())
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()

    def to_representation(self, instance):
        return {
            'total_movies': instance['total_movies'],
            'movies_by_genre': instance['movies_by_genre'],
            'total_reviews': instance['total_reviews'],
            'average_stars': round(instance['average_stars'], 2) if instance['average_stars'] else 0,
        }
