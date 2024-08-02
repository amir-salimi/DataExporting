from rest_framework import serializers

from .models import RealEstate


class RealEstateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = [
            'name', 'photo', 'link', 'property_types', 'service_areas',
            'properties', 'description', 'brn', 'arra', 'ded', 'phone_number'
        ]   

    def create(self, validated_data):
        validated_data["name"] = str(validated_data["name"]).lower()
        print(validated_data)
        real_estate, real_estate_created = RealEstate.objects.get_or_create(**validated_data)
        return real_estate