from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ResultViewset

router = DefaultRouter()
router.register('', ResultViewset, basename ='result')
app_name ='results'

urlpatterns=[
    path('', include(router.urls))
]