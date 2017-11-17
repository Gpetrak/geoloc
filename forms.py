from django.forms import Form, FloatField, CharField

class LookupForm(Form):
    latitude = FloatField()
    longitude = FloatField()
    layer = CharField(label='Select a layer', max_length=100)
      
