from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BranchesViewSet

router = DefaultRouter()
router.register('', BranchesViewSet, basename='branches')
app_name = 'branches'

urlpatterns = [
    path('', include(router.urls))
]