# Generated by Django 2.1.1 on 2018-09-24 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180912_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idioma',
            name='leng',
            field=models.CharField(blank=True, choices=[('spa', 'Español'), ('eng', 'English'), ('esp', 'Esperanto')], default='spa', help_text='Lenguaje del libro', max_length=15),
        ),
    ]
