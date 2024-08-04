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


class BuildingImgModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingImg
        fields = "__all__"


class BuildingDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingDetail
        fields = "__all__"
