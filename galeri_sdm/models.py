from django.db import models

# Create your models here.
class Infografis(models.Model):
    judul = models.CharField(db_column='Judul', max_length=255, blank=True, null=True)
    tumbnail = models.ImageField(db_column='Tumbnail', upload_to='media/infografis/thumbnails/', max_length=50, blank=True, null=True)
    lampiran = models.ImageField(db_column='Lampiran', upload_to='media/infografis/images/', blank=True)
    keterangan = models.TextField(db_column='Keterangan', blank=True, null=True)
    publish = models.BooleanField(db_column='Publish', blank=True, null=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True, auto_now_add=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'Web_Infografis'