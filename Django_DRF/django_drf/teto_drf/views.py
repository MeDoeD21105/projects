from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TetoSerializers

from .models import *
#4

class TetoAPIView(APIView):
    def get(self, request):
        w = Teto.objects.all()
        return Response({"posts": TetoSerializers(w, many = True).data})
    
    def post(self, request):
        serializer = TetoSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        post_new = Teto.objects.create(
            title = request.data["title"],
            content = request.data["content"],
            cat_id = request.data["cat_id"]
        )
        return Response({"post": TetoSerializers(post_new).data})
        

# Create your views here.
#class TetoAPIView(generics.ListAPIView):
#    queryset = Teto.objects.all()
#    serializer_class = TetoSerializer
