from django.db import models
import os

# Create your models here.
class Pengumuman(models.Model):
    judul = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/files/pengumuman/', blank=True)
    deskripsi = models.TextField()
    tanggalAwal = models.DateField(verbose_name='Tanggal Awal')
    tanggalAkhir = models.DateField(verbose_name='Tanggal Akhir')
    tanggalCreate = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(blank=True)

    def __str__(self):
        return self.judul

    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        db_table = 'web_pengumuman'