from rest_framework import serializers
from .models import Building, FullBuilding

class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = ('BBL', 'bin',  'datebuilt', 'roofheight', 'groundelevation',
                    'numfloors',  'centerlat', 'centerlon','streetaddress')


class FullBuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FullBuilding
        fields = ('bbl', 'bin',  'datebuilt', 'roofheight', 'groundelevation',
                    'numfloors',  'centerlat', 'centerlon','streetaddress')
