# from django import forms
from django.contrib.gis import forms
from .models import Servicio, Cliente

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        labels = {
            'nombre' : 'Nombre de Servicio:' 
        }
        widgets =  {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de Servicio'}),
        }

class ClienteForm(forms.ModelForm):
    # ubicacion = forms.PointField(widget=forms.OSMWidget(attrs={
    #     'class': 'form-control',
    #     # 'id': 'exampleFormControlTextarea1',
    #     # 'map_width': 80,
    #     # 'map_height': 500,
    #     'map_srid': 4326,
    #     'display_raw': False,
    #     'supports_3d': False,
    #     'dafault_zoom': 9,
    #     'default_lon': -66.158881515,
    #     'default_lat': -17.392562825,
    # }))
    class Meta:
        model = Cliente
        fields = ('nombre','direccion','telefono','ubicacion','servicio')
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de Cliente'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección de Cliente'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefono de Cliente'}),
            'servicio': forms.Select(attrs={'class':'form-control','placeholder':'Servicio'}),
        }
