from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Building, FullBuilding
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BuildingSerializer, FullBuildingSerializer
from bldgquery.find_close_buildings import building_finder

@api_view(['GET'])
def GetAllBuildings(request):
    if request.method == 'GET':
        numBuildings = request.GET.get('numBuildings', None)
        centerLat = request.GET.get('lat', None)
        centerLon = request.GET.get('lon', None)

        if (numBuildings is not None
            and centerLat is not None
            and centerLon is not None):
            # OLD, FUNCTIONAL bldgs=
            # bldgs = FullBuilding.objects.all()[:int(numBuildings)]
            # find_close_buildings Must take in GPS coord/numBuildings
            # and return valid queryset
            centerLat = float(centerLat)
            centerLon = float(centerLon)
            numBuildings = int(numBuildings)
            qs = building_finder(centerLat, centerLon, numBuildings)
            bldgs = FullBuilding.objects.filter(bin__in = qs)
            serializer = FullBuildingSerializer(bldgs, many=True)

            return Response(serializer.data)
        else:
            bldgs = Building.objects.all()
            serializer = BuildingSerializer(bldgs, many=True)
            return Response(serializer.data)

def LLInput(request, latInt, latDec, lonInt, lonDec):
    lat = latInt + '.' + latDec
    lat = float(lat)
    lon = lonInt + '.' + lonDec
    lon = float(lon)
    res = addTogether(lat,lon)
    context = {
        "lat": lat,
        "lon": lon,
        "res": res
    }
    return render(request, "latlontest.html", context)

def list_buildings(request):
    queryset = Building.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }

    return render(request, "index.html", context)

def bldgquery_home(request):
    return HttpResponse("<h1>Web query will go here.</h1>")

def lat_lon_query(request):
    return HttpResponse("<p>Lat/lon entered</p>")

def building_detail(request, bbl):
    instance = get_object_or_404(Building, BBL=bbl)
    context = {
        "title":instance.BBL,
        "instance": instance
    }
    return render(request, "building_detail.html", context)
