from django.shortcuts import render
from rest_framework import viewsets
from contact_us.models import contact_us
from contact_us.serializers import ContactUsSerializer

# Create your views here.

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = contact_us.objects.all()
    serializer_class = ContactUsSerializer
