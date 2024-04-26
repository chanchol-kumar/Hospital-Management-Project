from rest_framework import serializers
from service.models import service
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = '__all__'
