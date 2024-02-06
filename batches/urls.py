from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BatchesViewSet

router = DefaultRouter()
router.register('', BatchesViewSet, basename='batches')
app_name = 'batches'

urlpatterns = [
    path('', include(router.urls))
]