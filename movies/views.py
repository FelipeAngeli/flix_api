from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from movies.models import Movie
from movies.seriealizer import MovieModelSerializer, MovieStatsSerializer
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.ListAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, resquest):
        '''#Buscar todos os dados
        #Montar uma resposta
        #Devolver dados pro usuario com estatisticas'''

        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(total=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 2) if average_stars else 0,
        }

        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validate.data,
            status=status.HTTP_200_OK)
