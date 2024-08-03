from rest_framework import serializers

from .models import UnitPhoto, UnitDetail, UnitOfBuilding
from Building.models import Building
from RealEstate.models import Agency, Agent


class UnitPhotoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitPhoto
        fields = "__all__" 

    def create(self, validated_data):
        unit_photo, unit_photo_created = UnitPhoto.objects.get_or_create(**validated_data)
        return unit_photo


class UnitDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitDetail
        fields = "__all__"

    def create(self, validated_data):
        unit_detail, unit_detail_created = UnitDetail.objects.get_or_create(**validated_data)
        return unit_detail
    


class UnitModelSerializer(serializers.ModelSerializer):
    building_name = serializers.CharField()
    agent = serializers.CharField()
    agency = serializers.CharField()
    class Meta:
        model = UnitOfBuilding
        fields = ["building_name", "bed", "bath", "area", "description", 
                  "building_link", "price", "agent", "agency"
                ]

    def create(self, validated_data):
        validated_data["building_name"] = Building.objects.filter(name=str(validated_data.pop("building_name")).lower()).first()
        validated_data["agent"] = Agent.objects.filter(link=str(validated_data.pop("agent")).lower()).first()
        validated_data["agency"] = Agency.objects.filter(link=str(validated_data.pop("agency")).lower()).first()
        unit = UnitOfBuilding.objects.create(**validated_data)  
        unit.detail.add(*UnitDetail.objects.filter(building_link=validated_data["building_link"]))  
        unit.photo.add(*UnitPhoto.objects.filter(building_link=validated_data["building_link"]))
        return unit
