# serializers.py
from rest_framework import serializers

from .models import Finanzas

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finanzas
        fields = ('titulo', 'valor', 'fecha')