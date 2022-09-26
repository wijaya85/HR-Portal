from dataclasses import fields
from django import forms
from .models import Infografis, Banner, Video

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
        
        
class BannerForm(forms.ModelForm):
    # spesify the name
    class Meta:
        model = Banner
        fields = [
            'judul',
            'thumbnail',
            'gambar',
            'keterangan',
            'publish',
        ]
        widgets = {
            'publish': CheckBox(),
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            'judul', 
            'keterangan', 
            'thumbnail', 
            'lampiran', 
            'linkyoutube', 
            'publish'    
        ]
        widgets = {
            'publish': CheckBox(),
        }