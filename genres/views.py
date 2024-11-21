from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializer import GenreSerializer
from genres.permissions import GenrePermissionClass


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass) 
    queryset = Genre.objects.all() 
    serializer_class = GenreSerializer


class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass) 
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

