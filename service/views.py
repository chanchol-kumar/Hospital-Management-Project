from django.shortcuts import render
from rest_framework import viewsets
from service.models import service
from service.serializers import ServiceSerializer

# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = service.objects.all()
    serializer_class = ServiceSerializer
