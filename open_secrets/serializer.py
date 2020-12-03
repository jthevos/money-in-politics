from rest_framework import serializers
from .models import Legislator
from .models import Organization

class LegislatorSerializer(serializers.ModelSerializer):

    # def create(self, **kwargs):
    #     return Legislator.objects.create(kwargs)

    # def validate_cid(self, validated_data):
    #
    #     return True #Legislator.objects.create(**validated_data)
    # #cid = serializers.CharField(validators=[validate_cid()])

    # def validate(self):
    #     pass
    #
    # def to_internal_value(self, data):
    #     try:
    #         Legislator.objects.get(pk=data['cid'])
    #     except:
    #         Legislator.objects.create(data=data)


    class Meta:
        model = Legislator
        exclude = ['cid']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Organization
