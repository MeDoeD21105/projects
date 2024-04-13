from django.shortcuts import render
from rest_framework import generics
from .serializers import TetoSerializer

from .models import *
# Create your views here.
class TetoAPIView(generics.ListAPIView):
    queryset = Teto.objects.all()
    serializer_class = TetoSerializer