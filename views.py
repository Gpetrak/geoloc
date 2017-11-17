from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from geonode.geoloc.forms import LookupForm
from geonode.geoloc.models import Natura
from geonode.geoloc.models import Oikismoi
from geonode.geoloc.models import Loc
from django.contrib.gis.geos import Point
from django.contrib.gis.geos.geometry import GEOSGeometry
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
        layer = form.cleaned_data['layer']
 

        # Get Point
        location = Point(longitude, latitude, srid=4326)

        # check if in_out list is empty
        def inform_user(data, x): 
            if not x:
                result = "Your location is out of a %s region" % data
            else:
                result = "Your location is in %s region: %s" % (data, x[0])
            return result

        if layer == 'natura':
            # query to see if a point is in our out from a natura region
            in_out = Natura.objects.filter(geom__contains=location)
            result = inform_user(layer, in_out)
        if layer == 'oikismoi':
            in_out = Oikismoi.objects.filter(geom__contains=location)
            result = inform_user(layer, in_out)

        # Render the template
        return self.render_to_response({
                                  'result': result,
                                  'longitude': longitude,
                                  'latitude': latitude
                                 })


