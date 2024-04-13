from rest_framework import serializers
from .models import *


class TetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teto
        fields = ("title", "cat_id")