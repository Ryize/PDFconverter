# Generated by Django 3.2.4 on 2021-06-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDFconverter', '0002_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='files/%Y/%m/%d/'),
        ),
    ]
