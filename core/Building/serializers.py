from rest_framework import serializers


from area.models import City, Area
from .models import Building, Complex, BuildingHighlight, BuildingImg, BuildingDetail


class UpdateComplexPublishStatusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        fields = ["publish_status"]


class ComplexModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        # fields = "__all__"
        fields = ["name", "city", "area", "community", "buildings", "publish_status", "source"]


class BuildingHighlightModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingHighlight
        fields = "__all__"

    def create(self, validated_data):
        highlight, highlight_created = BuildingHighlight.objects.get_or_create(**validated_data)
        return highlight


class BuildingImgModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingImg
        fields = "__all__"

    def create(self, validated_data):
        image, image_created = BuildingImg.objects.get_or_create(**validated_data)
        return image


class BuildingDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingDetail
        fields = "__all__"
    
    def create(self, validated_data):
        detail, detail_created = BuildingDetail.objects.get_or_create(**validated_data)
        return detail


class BuildingModelSerializer(serializers.ModelSerializer):
    city = serializers.CharField()
    area = serializers.CharField(required=False)
    community = serializers.CharField(required=False)
    
    class Meta:
        model = Building
        fields = [
            "city", "area", "community", "name", "source", "building_link", 
            "status", "location", "about", "publish_status"
        ]

    def create(self, validated_data):

        City.objects.get_or_create(name=str(validated_data["city"]).lower())

        
        my_city = City.objects.filter(name=str(validated_data["area"])).first()
        if my_city:
            validated_data["city"] = my_city
            validated_data["area"] = None
            building = Building.objects.create(**validated_data)
            
        else:
            validated_data["city"] = City.objects.filter(name=str(validated_data["city"]).lower()).first()
            area, area_created = Area.objects.get_or_create(name=str(validated_data["area"]).lower, city=validated_data["city"])
            validated_data["area"] = area
            building = Building.objects.create(**validated_data)

        building.highlight.add(*BuildingHighlight.objects.filter(building_link=validated_data["building_link"]))
        building.img_link.add(*BuildingImg.objects.filter(building_link=validated_data["building_link"]))
        building.details.add(*BuildingDetail.objects.filter(building_link=validated_data["building_link"]))

        return building

