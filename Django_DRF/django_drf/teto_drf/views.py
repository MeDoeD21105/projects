from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import TetoSerializers
from rest_framework.decorators import action


# 9

class TetoViewSet(viewsets.ModelViewSet):
    queryset = Teto.objects.all()
    serializer_class = TetoSerializers
    
    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Teto.objects.all()

        return Teto.objects.filter(pk=pk)
    
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name + " Baka Jopa"})

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
