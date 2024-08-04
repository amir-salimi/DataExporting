from rest_framework import serializers

from .models import Building, Complex, BuildingHighlight, BuildingImg, BuildingDetail


class UpdateBuildingDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ["name", "source", "building_link", "status", "location","about", "publish_status"]


class UpdateComplexPublishStatusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        fields = ["publish_status"]


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


# class BuildingModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Building
#         fields = [
#             "city", "area", "community", "name", "source", "building_link", 
#             "status", "location", "about", "publish_status", "details", 
#             "img_link", "highlight"
#         ]

#     def create(self, validated_data):
#         return super().create(validated_data)

