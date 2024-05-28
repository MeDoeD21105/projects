from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TetoSerializers

from .models import *
#7

class TetoAPIList(generics.ListCreateAPIView):
    queryset = Teto.objects.all()
    serializer_class = TetoSerializers


class TetoAPIUpdate(generics.UpdateAPIView):
    queryset = Teto.objects.all()
    serializer_class  = TetoSerializers


class TetoAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teto.objects.all()
    serializer_class = TetoSerializers
    