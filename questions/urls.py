from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewset

router = DefaultRouter()
router.register('', QuestionViewset, basename ='question')
app_name ='question'

urlpatterns=[
    path('',include(router.urls))
]