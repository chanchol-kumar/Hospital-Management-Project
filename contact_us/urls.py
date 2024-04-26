from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contact_us.views import ContactUsViewSet

router = DefaultRouter() #our Router
router.register(r'contact_us', ContactUsViewSet,) # Antenna

urlpatterns = [
    path('', include(router.urls)),
]
