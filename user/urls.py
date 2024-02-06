from django.urls import path

from .views import ManageUserView, RegisterUserAPIView

app_name = 'user'

urlpatterns = [
    path('register', RegisterUserAPIView.as_view()),
    path('me', ManageUserView.as_view(),name="me")
]