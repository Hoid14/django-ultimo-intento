from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Finanzas


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Finanzas.objects.all().order_by('titulo')
    serializer_class = HeroSerializer

def finanzas_list(request):
    finanzas = Finanzas.objects.all()
    return render(request, 'finanzas_list.html', {'finanzas': finanzas})