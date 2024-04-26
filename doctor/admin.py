from django.contrib import admin
from doctor.models import Specialization,Designation,AvailableTime,Doctor,Review
# Register your models here.
admin.site.register(AvailableTime)

class specializationAdmin(admin. ModelAdmin): 
    prepopulated_fields = {"slug": ["name",]}
class designationAdmin(admin. ModelAdmin): 
    prepopulated_fields = {"slug": ["name",]}
    
admin.site.register(Designation,specializationAdmin)
admin.site.register(Specialization,designationAdmin)
admin.site.register(Doctor)
admin.site.register(Review)
