from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CoursesViewSet

router = DefaultRouter()
router.register('', CoursesViewSet, basename='courses')
app_name ='courses'

urlpatterns = [
    path('', include(router.urls))
]