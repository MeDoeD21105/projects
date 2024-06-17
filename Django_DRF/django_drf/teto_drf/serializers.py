from rest_framework import serializers

from .models import Teto


#6

class TetoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teto
        fields = "__all__"