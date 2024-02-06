"""HematiteAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt import authentication
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Hematite API",
      default_version='v1',
      description="Quiz App API",
      terms_of_service="http://hematitecorp.com/",
      contact=openapi.Contact(email="anmolchaware23@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   authentication_classes=(authentication.JWTAuthentication,),
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/voucher/',include('vouchers.urls')),
    path('api/enquirydetails/',include('enquirydetails.urls')),
    path('api/user/', include('user.urls')),
    path('api/feedbacks/',include('feedbacks.urls')),
    path('api/branches/',include('branches.urls')),
    path('api/courses/',include('courses.urls')),
    path('api/batches/',include('batches.urls')),
    path('api/exam/', include('exams.urls')),
    path('api/questions/', include('questions.urls')),
    path('api/students/', include('students.urls')),
    path('api/results/',include('results.urls')),
    path('api/enquiry/', include('enquiry.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/',swagger_auto_schema(methods=['post'],security=[])(TokenObtainPairView.as_view())),
    path('api/token/refresh/',swagger_auto_schema(methods=['post'],security=[])(TokenRefreshView.as_view())),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT,)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,)

