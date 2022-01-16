
from django.contrib import admin
from django.urls import path
from .views import Register, LoginAPIView, UserAPIView

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('users/', UserAPIView.as_view()),
]