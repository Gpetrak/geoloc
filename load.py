import os
from django.contrib.gis.utils import LayerMapping
from .models import Eparxiako_odiko_diktio

geoloc_mapping = {
    'aa' : 'aa',
    'yparith' : 'YpArith',
    'onomasia' : 'Onomasia',
    'katataksi' : 'Katataksi',
    'tmima' : 'Tmima',
    'apallotr' : 'Apallotr',
    'fekapall' : 'FEKapall',
    'arfakellou' : 'ArFakellou',
    'sxolia' : 'Sxolia',
    'parakatath' : 'Parakatath',
    'yp' : 'Yp',
    'geom' : 'MULTILINESTRING',
}


geoloc_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Eparxiako_odiko_diktio.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
         Eparxiako_odiko_diktio, geoloc_shp, 
         geoloc_mapping, transform=False,
         encoding='iso-8859-7',
    )
    lm.save(strict=True, verbose=verbose)


