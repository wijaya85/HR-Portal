from django.db import models

# Create your models here.
class TempDataLengkap092022(models.Model):
    idpegawai = models.IntegerField(db_column='IDPegawai')
    nip = models.CharField(db_column='NIP', max_length=18, blank=True, null=True)
    nipbaru = models.CharField(db_column='NIPBaru', max_length=18, blank=True, null=True)
    namalengkap = models.CharField(db_column='NamaLengkap', max_length=8000, blank=True, null=True)
    kodekelamin = models.CharField(db_column='KodeKelamin', max_length=1)
    kodegolongan = models.CharField(db_column='KodeGolongan', max_length=5, blank=True, null=True)
    kodegolonganruang = models.CharField(db_column='KodeGolonganRuang', max_length=5, blank=True, null=True)
    jenjangjabatan = models.CharField(db_column='JenjangJabatan', max_length=50, blank=True, null=True)
    jabatan = models.CharField(db_column='Jabatan', max_length=255, blank=True, null=True)
    singkatanjenjang = models.CharField(db_column='SingkatanJenjang', max_length=5, blank=True, null=True)
    pendidikan = models.CharField(db_column='Pendidikan', max_length=50, blank=True, null=True)
    esl1 = models.TextField(db_column='Esl1')
    esl2 = models.TextField()
    esl3 = models.TextField()
    esl4 = models.TextField()
    tahunpensiun = models.IntegerField(db_column='TahunPensiun', blank=True, null=True)
    statuspegawai = models.CharField(db_column='StatusPegawai', max_length=100, blank=True, null=True)
    ckp = models.FloatField(db_column='CKP')
    np = models.FloatField(db_column='NP')
    generasi = models.CharField(db_column='Generasi', max_length=11, blank=True, null=True)
    provinsikantor = models.CharField(db_column='ProvinsiKantor', max_length=50, blank=True, null=True)
    kotakantor = models.CharField(db_column='KotaKantor', max_length=50, blank=True, null=True)
    unitsingkat = models.TextField(db_column='UnitSingkat', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Temp_Data_lengkap_092022'
        
 
        
class Statistikpegawaiperuniteselon1(models.Model):
    singkatanesl1 = models.TextField(db_column='singkatanEsl1')  # Field name made lowercase.
    jumlah = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'statistikPegawaiPerUnitEselon1'