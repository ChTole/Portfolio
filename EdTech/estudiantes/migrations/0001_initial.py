# Generated by Django 4.0.5 on 2022-07-21 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoInscripto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso_inscripto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.comision')),
            ],
        ),
    ]
