from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EnquiryViewset

router = DefaultRouter()
router.register('', EnquiryViewset, basename ='enquiry')
app_name ='enquiry'

urlpatterns=[
    path('', include(router.urls))
]