from django.shortcuts import render
from rest_framework import viewsets
from patient.models import patient
from patient.serializers import PatientSerializer

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = PatientSerializer
