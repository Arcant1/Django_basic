# Generated by Django 2.1.1 on 2018-09-07 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180906_2209'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lenguaje',
            new_name='Idioma',
        ),
        migrations.RemoveField(
            model_name='instancia',
            name='lenguaje',
        ),
        migrations.AddField(
            model_name='libro',
            name='lenguaje',
            field=models.ManyToManyField(help_text='Seleccione un idioma para el libro', to='catalog.Idioma'),
        ),
    ]