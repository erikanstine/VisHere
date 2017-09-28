from django.conf.urls import url, include
from bldgquery.views import bldgquery_home,lat_lon_query, building_detail, list_buildings, LLInput
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', list_buildings),
    url(r'^llquery/$', lat_lon_query),
    url(r'^detail/(?P<bbl>\d+)/$', building_detail),
    # api
    url(r'^query/$', views.GetAllBuildings),

    url(r'^latlontest/lat=(?P<latInt>\d+).(?P<latDec>\d+)&lon=(?P<lonInt>\d+).(?P<lonDec>\d+)/$', LLInput),

]
