from django.db import models

# Create your models here.
class Infografis(models.Model):
    judul = models.CharField(db_column='Judul', max_length=255, blank=True, null=True)
    tumbnail = models.ImageField(db_column='Tumbnail', upload_to='media/infografis/thumbnails/', blank=True, null=True)
    lampiran = models.ImageField(db_column='Lampiran', upload_to='media/infografis/images/', blank=True)
    keterangan = models.TextField(db_column='Keterangan', blank=True, null=True)
    publish = models.BooleanField(db_column='Publish', blank=True, null=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True, auto_now_add=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'Web_Infografis'

        
class Banner(models.Model):
    judul = models.CharField(db_column='judul', max_length=50, blank=True)
    thumbnail = models.ImageField(db_column='thumbnail', upload_to='media/banner/thumbnails', blank=True, null=True)
    gambar = models.ImageField(db_column='gambar', upload_to='media/banner/images')
    keterangan = models.TextField(db_column='keterangan', blank=True, null=True)
    publish = models.BooleanField(db_column='publish', blank=True, null=True)
    createddate = models.DateTimeField(db_column='CreatedDate', auto_now_add=True)
    createdby = models.IntegerField(db_column='CreateBy', blank=True, null=True)
    
    class Meta:
        db_table = 'Web_Banner'


class Video(models.Model):
    judul = models.CharField(db_column='judul', max_length=100)
    keterangan = models.TextField(db_column='keterangan', blank=True, null=True)
    thumbnail = models.ImageField(db_column='thumbnail', upload_to='media/video/thumbnails', blank=True, null=True)
    lampiran = models.FileField(db_column='Lampiran', upload_to='media/video/', blank=True, null=True)
    linkyoutube = models.CharField(db_column='LinkYoutube', max_length=100, blank=True, null=True)
    publish = models.BooleanField(db_column='publish', blank=True, null=True)
    createddate = models.DateTimeField(db_column='CreatedDate', auto_now_add=True)
    createdby = models.IntegerField(db_column='CreateBy', blank=True, null=True)
    
    class Meta:
        db_table = 'web_video'