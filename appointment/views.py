from django.shortcuts import render
from rest_framework import viewsets
from appointment.models import Appointment
from appointment.serializers import AppoinmentSerializer

# Create your views here.

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppoinmentSerializer
    
def get_queryset(self):
    queryset = super().get_queryset()
    patient_id = self.request.query_param.get('patient_id')
    if patient_id:
        queryset = queryset.filter(patient_id=patient_id)
    return queryset
    

