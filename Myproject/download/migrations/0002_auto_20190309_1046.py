# Generated by Django 2.0.3 on 2019-03-09 02:46

from django.db import migrations, models
import download.filesstorage


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='filepath',
            field=models.FileField(storage=download.filesstorage.FilesStorage(), upload_to='files/download'),
        ),
        migrations.AlterField(
            model_name='download',
            name='imgpath',
            field=models.ImageField(storage=download.filesstorage.ImageStorage(), upload_to='files/download'),
        ),
    ]
