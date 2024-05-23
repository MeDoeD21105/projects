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
        serializer.save()
        return Response({"post": serializer.data})


    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT now allowed"})
        
        try:
            instance = Teto.objects.get(pk=pk)
        except:
            return Response({"error": "Object does now exists"})
        
        serilizer = TetoSerializers(data=request.data, instance=instance)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response({"post": serilizer.data})