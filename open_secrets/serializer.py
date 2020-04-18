from rest_framework import serializers
from .models import Legislator

class LegislatorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Legislator
