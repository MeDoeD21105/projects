from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TetoSerializer

from .models import *


class TetoAPIView(APIView):
    def get(self, request):
        lst = Teto.objects.all().values()
        return Response({"posts": list(lst)})

# Create your views here.
#class TetoAPIView(generics.ListAPIView):
#    queryset = Teto.objects.all()
#    serializer_class = TetoSerializer
