from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FeedbacksViewSet

router = DefaultRouter()
router.register('', FeedbacksViewSet, basename='feedbacks')
app_name ='feedbacks'

urlpatterns = [
    path('', include(router.urls))
]