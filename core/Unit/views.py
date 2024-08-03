from django.http import HttpResponse

from rest_framework.viewsets import generics

from .models import UnitDetail, UnitOfBuilding, UnitPhoto
from .serializers import UnitPhotoModelSerializer, UnitDetailModelSerializer, UnitModelSerializer



class HttpResponseOk(HttpResponse):
    status_code = 200


class UnitPhotoSet(generics.CreateAPIView):
    queryset = UnitPhoto.objects.all()
    serializer_class = UnitPhotoModelSerializer


class UnitDetailSet(generics.CreateAPIView):
    queryset = UnitDetail.objects.all()
    serializer_class = UnitDetailModelSerializer


class UnitSet(generics.CreateAPIView):
    queryset = UnitOfBuilding.objects.all()
    serializer_class = UnitModelSerializer


