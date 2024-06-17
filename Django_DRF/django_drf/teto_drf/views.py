from rest_framework import viewsets

from .models import *
from .serializers import TetoSerializers


# 7

class TetoViewSet(viewsets.ModelViewSet):
    queryset = Teto.objects.all()
    serializer_class = TetoSerializers

# class TetoAPIList(generics.ListCreateAPIView):
#     queryset = Teto.objects.all()
#     serializer_class = TetoSerializers
#
#
# class TetoAPIUpdate(generics.UpdateAPIView):
#     queryset = Teto.objects.all()
#     serializer_class  = TetoSerializers
#
#
# class TetoAPIList(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Teto.objects.all()
#     serializer_class = TetoSerializers
