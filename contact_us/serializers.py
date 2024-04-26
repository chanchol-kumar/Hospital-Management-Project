from rest_framework import serializers
from contact_us.models import contact_us
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_us
        fields = '__all__'
