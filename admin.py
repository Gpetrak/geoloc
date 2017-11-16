from django.contrib import admin
from geonode.geoloc.models import Loc, EparxiakoOdikoDiktio
from django.forms import ModelForm
from floppyforms.gis import PointWidget, BaseGMapWidget

class CustomPointWidget(PointWidget, BaseGMapWidget):

    class Media:

        js = ('/home/gpetr/venv_2.7/geonode/geonode/static_root/floppyforms/js',)

class LocAdminForm(ModelForm):
    class Meta:
        model = Loc
        fields = ['name', 'location']
        widgets = {
            'location': CustomPointWidget()
    }

class LocAdmin(admin.ModelAdmin):
    form = LocAdminForm

class EparxiakoOdikoDiktioAdminForm(ModelForm):
    class Meta:
        model = EparxiakoOdikoDiktio
        fields = ['onomasia', 'geom']
        widgets = { 
            'geom' : CustomPointWidget()
       }

class EparxiakoOdikoDiktioAdmin(admin.ModelAdmin):
    form = EparxiakoOdikoDiktioAdminForm


admin.site.register(Loc, LocAdmin)
admin.site.register(EparxiakoOdikoDiktio, EparxiakoOdikoDiktioAdmin)
