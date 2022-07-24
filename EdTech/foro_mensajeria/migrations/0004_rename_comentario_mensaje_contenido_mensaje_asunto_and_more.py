# Generated by Django 4.0.5 on 2022-07-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro_mensajeria', '0003_alter_comentario_imagen_alter_comentario_posteo_rel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='comentario',
            new_name='contenido',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='asunto',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Asunto'),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='mensajes'),
        ),
    ]
