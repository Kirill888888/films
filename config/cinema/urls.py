from django.urls import path
from cinema.views import movies


urlpatterns = [
    path('',movies)
]