from django import forms
from .models import Pengumuman

class DateInput(forms.DateInput):
    input_type = 'date'
    
class CheckBox(forms.CheckboxInput):
    input_type =  'checkbox'

class PengumumanForm(forms.ModelForm):
    # spesify the name
    class Meta:
        model = Pengumuman
        fields = [
            'judul',
            'file',
            'tanggalAwal',
            'tanggalAkhir',
            'publish',
            'deskripsi'
        ]
        widgets = {
            'tanggalAwal': DateInput(),
            'tanggalAkhir': DateInput(),
            'publish': CheckBox(),
        }