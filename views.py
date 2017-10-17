from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from geonode.geoloc.forms import LookupForm
from geonode.geoloc.models import OdikoDiktyoKritis
from geonode.geoloc.models import Loc
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D # 'D' is a shortcut for 'Distance'
from django.template import RequestContext
from django.core.serializers import serialize
import json, ast


class LookupView(FormView):
    # template that is rendered when the form is valid
    template_name = 'geoloc/lookupresults.html'
    form_class = LookupForm
    # success_url = '/gigs/'
    
    def get(self, request): 
        return render_to_response('geoloc/lookup.html', RequestContext(request))
    
    def form_valid(self, form):
        # Get data
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']
 
        # Get distance
        distance = form.cleaned_data['distance'] 

        # Get Point
        location = Point(longitude, latitude, srid=4326)


        # find the roads in a distance of 40 km from my location
        roads = OdikoDiktyoKritis.objects.filter(geom__distance_lte=(location, D(km=distance)))
   
        roads_json = serialize('geojson', roads, 
                   fields=('geom',))
        
        # remove crs key from geojson object because it is not recommended
        # and it raises invalid geojson object
        new_roads_json = json.loads(roads_json)
        new_roads_json.pop('crs', None)
        new_roads_json = json.dumps(new_roads_json)
     
        # Render the template
        return self.render_to_response({
                                  'new_roads_json': new_roads_json,
                                  'longitude': longitude,
                                  'latitude': latitude
                                 })


