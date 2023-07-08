# Generated by Django 4.2.2 on 2023-07-08 20:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0009_alter_pantalon_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pantalon',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pantalon',
            name='fecha_publicacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
