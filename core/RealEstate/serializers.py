from rest_framework import serializers

from .models import Agency, Agent


class RealEstateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = [
            'name', 'photo', 'link', 'property_types', 'service_areas',
            'properties', 'description', 'brn', 'arra', 'ded', 'phone_number'
        ]   

    def create(self, validated_data):
        validated_data["name"] = str(validated_data["name"]).lower()
        print(validated_data)
        real_estate, real_estate_created = Agency.objects.get_or_create(**validated_data)
        return real_estate
    

class AgentModelSerializer(serializers.ModelSerializer):
    agency = serializers.CharField() 
    class Meta:
        model = Agent
        fields = [
            "name","link","photo","languages","specialities","service_areas",
            "properties","description","experience","phone_number","brn","agency"
        ]

    def create(self, validated_data):
        validated_data["name"] = str(validated_data["name"]).lower()
        validated_data["agency"] = Agency.objects.filter(name=str(validated_data.pop("agency")).lower()).first()
        print(validated_data["agency"])
        agent, agent_created = Agent.objects.get_or_create(**validated_data)
        return agent

