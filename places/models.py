from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=150)
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Длинное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longtitude = models.FloatField(verbose_name='Долгота')

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
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    
    class Meta:
        ordering = ['order'] 
    
    def __str__(self):
        return f"{self.order} {self.place.title}"