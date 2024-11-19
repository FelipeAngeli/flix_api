
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    #authentication
    path('api/v1/', include('authentication.urls')),
    #genres
    path('api/v1/', include('genres.urls')),
    #actors
    path('api/v1/', include('actors.urls')),
    #movies
    path('api/v1/', include('movies.urls')),
    #reviews
    path('api/v1/', include('reviews.urls')),

]
