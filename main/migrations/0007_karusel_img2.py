# Generated by Django 4.2.3 on 2023-07-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_karusel_passive_delete_passive'),
    ]

    operations = [
        migrations.AddField(
            model_name='karusel',
            name='img2',
            field=models.ImageField(default=1, upload_to='my_images', verbose_name='karusel image2'),
            preserve_default=False,
        ),
    ]
