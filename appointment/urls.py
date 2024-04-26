from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appointment.views import AppointmentViewSet

router = DefaultRouter() #our Router
router.register(r'appointment', AppointmentViewSet,) # Antenna

urlpatterns = [
    path('', include(router.urls)),
]
