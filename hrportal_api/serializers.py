from dataclasses import fields
from rest_framework import serializers
from pengumuman.models import Pengumuman

class PengumumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengumuman
        fields = '__all__'