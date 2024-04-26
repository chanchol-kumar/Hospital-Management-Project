from django.urls import path, include
from rest_framework.routers import DefaultRouter
from service.views import ServiceViewSet

router = DefaultRouter() #our Router
router.register(r'contact_us', ServiceViewSet,) # Antenna

urlpatterns = [
    path('', include(router.urls)),
]
