# Generated by Django 3.1.7 on 2021-04-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_auto_20210405_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='pdf',
            field=models.FileField(blank=True, upload_to='upload_pdf/'),
        ),
    ]
