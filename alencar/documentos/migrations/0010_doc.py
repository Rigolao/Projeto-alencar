# Generated by Django 3.1.7 on 2021-04-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0009_edocmodel_pasta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]