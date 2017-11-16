from django.conf.urls import patterns, url
from geonode.geoloc.views import LookupView

urlpatterns = patterns(
    'geonode.geoloc.views',
    url(r'^$',  LookupView.as_view(), name='lookup'),
    )

