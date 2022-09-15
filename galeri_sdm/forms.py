from django import forms
from .models import Infografis

class CheckBox(forms.CheckboxInput):
    input_type =  'checkbox'

class InfografisForm(forms.ModelForm):
    # spesify the name
    class Meta:
        model = Infografis
        fields = [
            'judul',
            'tumbnail',
            'lampiran',
            'keterangan',
            'publish',
        ]
        widgets = {
            'publish': CheckBox(),
        }