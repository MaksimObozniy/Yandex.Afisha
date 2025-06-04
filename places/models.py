from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=150)
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Длинное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longtitude = models.FloatField(verbose_name='Долгота')
    
    imgs = models.JSONField(verbose_name='Ссылки на фотографии', blank=True)

    def __str__(self):
        return self.title
        