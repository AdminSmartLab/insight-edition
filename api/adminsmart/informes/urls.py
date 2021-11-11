from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import InformesViewSet

router = DefaultRouter()

router.register(r'', InformesViewSet, base_name='informes')

urlpatterns = [
     path('', include(router.urls))
]