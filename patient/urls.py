from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patient.views import PatientViewSet

router = DefaultRouter() #our Router
router.register(r'patient', PatientViewSet,) # Antenna

urlpatterns = [
    path('', include(router.urls)),
]
