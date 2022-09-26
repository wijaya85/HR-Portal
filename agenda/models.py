from django.db import models
import os

# Create your models here.
class RefAgenda(models.Model):
    jenisAgenda = models.CharField(max_length=50) #offline/ online/ hybrid
    keterangan = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'Web_RefAgenda'

        
class Agenda(models.Model):
    judul = models.CharField(max_length=255)
    jenis = models.ForeignKey('RefAgenda', on_delete=models.CASCADE)
    tanggalMulai = models.DateTimeField()
    tanggalSelesai = models.DateTimeField()
    tempat = models.CharField(max_length=255)
    linkMeeting = models.CharField(max_length=255)
    keterangan = models.CharField(max_length=255)
    createdBy = models.IntegerField()
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedBy = models.IntegerField()
    updatedDate = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='media/files/agenda/', blank=True)

    class Meta:
        db_table = 'Web_Agenda'