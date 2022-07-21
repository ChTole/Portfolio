# Generated by Django 4.0.5 on 2022-07-21 15:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=50, unique=True, verbose_name='Título curso')),
            ],
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_comision', models.PositiveIntegerField(unique=True, verbose_name='Comisión Nro.')),
                ('vacantes', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Vacantes')),
                ('tema_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.tema')),
            ],
        ),
    ]