from django.shortcuts import render
from .serializers import SingerSerializers, SongSerializers
from rest_framework import viewsets
from .models import Singer, Song


# Create your views here.
class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializers


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers
