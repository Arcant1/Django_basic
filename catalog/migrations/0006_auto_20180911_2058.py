# Generated by Django 2.1.1 on 2018-09-11 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180906_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='lenguaje',
        ),
        migrations.AddField(
            model_name='libro',
            name='lenguaje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Idioma'),
        ),
    ]
