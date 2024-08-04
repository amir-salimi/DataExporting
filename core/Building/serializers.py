from rest_framework import serializers

from .models import Building, Complex


class UpdateBuildingDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ["name", "source", "building_link", "status", "location","about", "publish_status"]


class UpdateComplexPublishStatusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        fields = ["publish_status"]
