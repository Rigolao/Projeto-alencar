# Generated by Django 3.1.7 on 2021-04-07 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0006_pasta'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasta',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
