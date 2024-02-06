from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ExamViewset

router =DefaultRouter()
router.register('', ExamViewset, basename='exam')
app_name ='exams'

urlpatterns=[
    path('', include(router.urls))
]