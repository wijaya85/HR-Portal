from django.db import models

# Create your models here.
class DataLengkap(models.Model):
    idpegawai = models.IntegerField(db_column='IDPegawai', primary_key=True)
    nip = models.CharField(db_column='NIP', max_length=18, blank=True, null=True)
    nipbaru = models.CharField(db_column='NIPBaru', max_length=18, blank=True, null=True)
    namalengkap = models.CharField(db_column='NamaLengkap', max_length=8000, blank=True, null=True)
    kodekelamin = models.CharField(db_column='KodeKelamin', max_length=1)
    kodegolongan = models.CharField(db_column='KodeGolongan', max_length=5, blank=True, null=True)
    kodegolonganruang = models.CharField(db_column='KodeGolonganRuang', max_length=5, blank=True, null=True)
    tmtpangkat = models.DateTimeField(db_column='TMTPangkat', blank=True, null=True)
    jenjangjabatan = models.CharField(db_column='JenjangJabatan', max_length=50, blank=True, null=True)
    jabatan = models.CharField(db_column='Jabatan', max_length=255, blank=True, null=True)
    tmtjabatan = models.DateTimeField(db_column='TMTJabatan', blank=True, null=True)
    singkatanjenjang = models.CharField(db_column='SingkatanJenjang', max_length=5, blank=True, null=True)
    pendidikan = models.CharField(db_column='Pendidikan', max_length=50, blank=True, null=True)
    jurusan = models.CharField(db_column='Jurusan', max_length=250)
    namalembagapendidikan = models.CharField(db_column='NamaLembagaPendidikan', max_length=100)
    tanggallulus = models.DateField(db_column='TanggalLulus', blank=True, null=True)
    namaprogramstudi = models.CharField(db_column='NamaProgramStudi', max_length=255, blank=True, null=True)
    namaprogramstudiluarnegeri = models.CharField(db_column='NamaProgramStudiLuarNegeri', max_length=255, blank=True, null=True)
    idjabatan = models.IntegerField(db_column='IDJabatan', blank=True, null=True)
    idorganisasi = models.IntegerField(db_column='IDOrganisasi', blank=True, null=True)
    kodeorganisasi = models.CharField(db_column='KodeOrganisasi', max_length=20, blank=True, null=True)
    esl1 = models.TextField(db_column='Esl1')
    esl2 = models.TextField(db_column='Esl2')
    esl3 = models.TextField(db_column='Esl3')
    esl4 = models.TextField(db_column='Esl4')
    esl5 = models.TextField(db_column='Esl5')
    kodesatker = models.CharField(db_column='KodeSatker', max_length=6, blank=True, null=True)
    rangeusia = models.CharField(db_column='RangeUsia', max_length=10)
    usiatahun = models.IntegerField(db_column='UsiaTahun', blank=True, null=True)
    usiabulan = models.IntegerField(db_column='UsiaBulan', blank=True, null=True)
    tanggallahir = models.DateTimeField(db_column='TanggalLahir', blank=True, null=True)
    tmtpensiun = models.DateTimeField(db_column='TmtPensiun', blank=True, null=True)
    tahunpensiun = models.IntegerField(db_column='TahunPensiun', blank=True, null=True)
    tmtkenaikanpangkatberikutnya = models.DateTimeField(db_column='TMTKenaikanPangkatBerikutnya', blank=True, null=True)
    statuspegawai = models.CharField(db_column='StatusPegawai', max_length=100, blank=True, null=True)
    keterangantambahan = models.CharField(db_column='KeteranganTambahan', max_length=255)
    tempatlahir = models.CharField(db_column='TempatLahir', max_length=60, blank=True, null=True)
    masakerjatahun = models.IntegerField(blank=True, null=True)
    grading = models.IntegerField(db_column='Grading')
    idrefeselon = models.IntegerField(db_column='IDRefEselon', blank=True, null=True)
    idreftingkatpendidikan = models.IntegerField(db_column='IDRefTingkatPendidikan', blank=True, null=True)
    tmtstatuspegawai = models.DateTimeField(db_column='TMTStatusPegawai', blank=True, null=True)
    generasi = models.CharField(db_column='Generasi', max_length=11, blank=True, null=True)
    jenisjabatan = models.CharField(db_column='JenisJabatan', max_length=100, blank=True, null=True)
    jpm = models.FloatField(db_column='JPM')
    rangejpm = models.CharField(db_column='RangeJPM', max_length=4)
    tanggalac = models.DateTimeField(db_column='TanggalAC')
    ckp = models.FloatField(db_column='CKP')
    np = models.FloatField(db_column='NP')
    nkp = models.FloatField(db_column='NKP')
    ppkp = models.FloatField(db_column='PPKP')
    kriterianp = models.CharField(db_column='KriteriaNP', max_length=9)
    kriteriappkp = models.CharField(db_column='KriteriaPPKP', max_length=6)
    tahunlulus = models.IntegerField(db_column='TahunLulus', blank=True, null=True)
    lokasipendidikan = models.CharField(db_column='LokasiPendidikan', max_length=12)
    jenisorganisasi = models.CharField(db_column='JenisOrganisasi', max_length=50, blank=True, null=True)
    jenisijinpendidikan = models.CharField(db_column='JenisIjinPendidikan', max_length=25)
    jeniskepegawaian = models.CharField(db_column='JenisKepegawaian', max_length=255)
    tipeorganisasi = models.CharField(db_column='TipeOrganisasi', max_length=255, blank=True, null=True)  # Field name made lowercase.    
    masakerjajabatan = models.IntegerField(db_column='MasaKerjaJabatan', blank=True, null=True)  # Field name made lowercase.
    provinsikantor = models.CharField(db_column='ProvinsiKantor', max_length=50, blank=True, null=True)  # Field name made lowercase.     
    instansidpkdpb = models.CharField(db_column='InstansiDpkDpb', max_length=255, blank=True, null=True)  # Field name made lowercase.    
    jeniskantor = models.CharField(db_column='JenisKantor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    statuspernikahan = models.CharField(db_column='StatusPernikahan', max_length=50, blank=True, null=True)  # Field name made lowercase. 
    jenjang = models.CharField(db_column='Jenjang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kotakantor = models.CharField(db_column='KotaKantor', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_lengkap'