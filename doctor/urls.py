from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctor.views import DoctorViewSet,SpecializationViewSet,DesignationViewSet,AvailableTimeViewSet,ReviewViewSet

router = DefaultRouter() #our Router
router.register(r'Doctor', DoctorViewSet,) # Antenna
router.register(r'Specialization', SpecializationViewSet,) # Antenna
router.register(r'Designation', DesignationViewSet,) # Antenna
router.register(r'AvailableTime', AvailableTimeViewSet,) # Antenna
router.register(r'Review', ReviewViewSet,) # Antenna

urlpatterns = [
    path('', include(router.urls)),
]
