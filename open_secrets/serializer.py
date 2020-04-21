from rest_framework import serializers
from .models import Legislator
from .models import Organization

class LegislatorSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Legislator.objects.create(**validated_data)
        
    class Meta:
        fields = '__all__'
        model = Legislator


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Organization
