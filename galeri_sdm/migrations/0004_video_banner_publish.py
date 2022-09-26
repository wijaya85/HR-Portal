# Generated by Django 4.0 on 2022-09-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri_sdm', '0003_banner_delete_webinfografis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(db_column='judul', max_length=100)),
                ('keterangan', models.TextField(blank=True, db_column='keterangan', null=True)),
                ('thumbnail', models.ImageField(blank=True, db_column='thumbnail', null=True, upload_to='media/video/thumbnails')),
                ('lampiran', models.FileField(blank=True, db_column='Lampiran', null=True, upload_to='media/video/')),
                ('linkyoutube', models.CharField(blank=True, db_column='LinkYoutube', max_length=100, null=True)),
                ('publish', models.BooleanField(blank=True, db_column='publish', null=True)),
                ('createddate', models.DateTimeField(auto_now_add=True, db_column='CreatedDate')),
                ('createdby', models.IntegerField(blank=True, db_column='CreateBy', null=True)),
            ],
            options={
                'db_table': 'web_video',
            },
        ),
        migrations.AddField(
            model_name='banner',
            name='publish',
            field=models.BooleanField(blank=True, db_column='publish', null=True),
        ),
    ]
