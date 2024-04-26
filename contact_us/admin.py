from django.contrib import admin
from contact_us.models import contact_us
# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["name","phone","problem"]
admin.site.register(contact_us,ContactModelAdmin)
