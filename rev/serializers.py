from rest_framework.renderers import JSONRenderer, JSONOpenAPIRenderer
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields= ['name', 'hotel_detail','image', 'review', 'rev_stars',  ]
        
        
