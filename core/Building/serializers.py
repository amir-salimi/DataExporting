from rest_framework import serializers


from area.models import City, Area, Community
from .models import Building, Complex, BuildingHighlight, BuildingImg, BuildingDetail


class UpdateComplexPublishStatusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        fields = ["publish_status"]


class UpdateComplexBuildingModelSerializer(serializers.HyperlinkedModelSerializer):
    buildings = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    class Meta:
        model = Complex
        fields = ["buildings", "name"]

    def update(self, instance, validated_data):
        return instance.buildings.add(Building.objects.filter(name=str(validated_data["buildings"]).lower()).first())


class ComplexModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
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
        print(validated_data["area"])


        # City.objects.get_or_create(name=str(validated_data["city"]).lower())
        # try:
        #     validated_data["city"] = City.objects.filter(name=str(validated_data["area"]).lower()).get()
        #     Building.objects.create(**validated_data)
        # except:
        #     validated_data["city"] = City.objects.get_or_create(name=str(validated_data["city"]).lower())
        #     validated_data["area"] = Area.objects.get_or_create(name=str(validated_data["area"]).lower, city=validated_data["city"])
        #     building = Building.objects.create(**validated_data)
        



        # return super().create(validated_data)

