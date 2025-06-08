from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название места')
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    long_description = HTMLField(verbose_name='Длинное описание', blank=True)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'
    )

    image = models.ImageField(upload_to='places/', verbose_name="Картинка")
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок', db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}{self.place.title}"
