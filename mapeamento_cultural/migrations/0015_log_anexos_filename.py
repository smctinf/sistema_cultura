# Generated by Django 3.2.13 on 2022-08-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapeamento_cultural', '0014_rename_id_artista_log_anexos_artista'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_anexos',
            name='filename',
            field=models.CharField(default='', max_length=150, verbose_name='Anexo'),
            preserve_default=False,
        ),
    ]