
from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from .views import  ReviewViewSet
from django.urls import path, include

router = DefaultRouter()

router.register(r'review', ReviewViewSet, basename='review')



urlpatterns = [
    path('', include(router.urls) )
]

