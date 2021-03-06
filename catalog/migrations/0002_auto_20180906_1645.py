# Generated by Django 2.1.1 on 2018-09-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='genre',
            new_name='genero',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='summary',
        ),
        migrations.AddField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(default='Sin descripción', help_text='Enter a brief description of the book', max_length=1000),
        ),
    ]
