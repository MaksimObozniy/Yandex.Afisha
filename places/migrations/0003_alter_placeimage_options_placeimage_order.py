# Generated by Django 5.2.1 on 2025-06-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_remove_place_imgs_placeimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='placeimage',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
    ]
