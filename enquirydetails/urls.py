from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EnquiryViewSet

router = DefaultRouter()
router.register('', EnquiryViewSet, basename='enquiry')
app_name = 'enquiry'

urlpatterns=[
    path('', include(router.urls))
]