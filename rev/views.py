
from django.shortcuts import render
from .models import  Review
from .serializers import  ReviewSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
  

   








