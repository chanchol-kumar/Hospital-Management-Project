from django.contrib import admin
from patient.models import patient

class PatientAdminModel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'image']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

admin.site.register(patient, PatientAdminModel)
