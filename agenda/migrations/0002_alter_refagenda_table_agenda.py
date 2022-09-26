# Generated by Django 4.0 on 2022-09-13 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='refagenda',
            table='Web_RefAgenda',
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('tanggalMulai', models.DateTimeField()),
                ('tanggalSelesai', models.DateTimeField()),
                ('tempat', models.CharField(max_length=255)),
                ('linkMeeting', models.CharField(max_length=255)),
                ('keterangan', models.CharField(max_length=255)),
                ('createdBy', models.IntegerField()),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedBy', models.IntegerField()),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, upload_to='media/files/agenda/')),
                ('jenis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.refagenda')),
            ],
            options={
                'db_table': 'Web_Agenda',
            },
        ),
    ]
