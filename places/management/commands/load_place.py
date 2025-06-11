import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Загружает место из JSON по ссылке'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='Ссылка на JSON')

    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()
        place_info = response.json()

        place, created = Place.objects.get_or_create(
            title=place_info['title'],
            defaults={
                'short_description': place_info.get('description_short', ''),
                'long_description': place_info.get('description_long', ''),
                'latitude': place_info['coordinates']['lat'],
                'longitude': place_info['coordinates']['lng'],
            }
        )

        if not created:
            self.stdout.write(
                self
                .style
                .WARNING(f'Место "{place.title}" уже есть'))
        else:
            self.stdout.write
            (self
             .style
             .SUCCESS(f'Создано место: {place.title}'))

        for idx, img_url in enumerate(place_info.get('imgs', []), start=1):
            img_response = requests.get(img_url)
            img_response.raise_for_status()
            img_name = img_url.split('/')[-1]
            image = PlaceImage(place=place, order=idx)
            image.image.save(
                img_name,
                ContentFile(img_response.content), save=True)
            self.stdout.write(
                self
                .style
                .SUCCESS(f'Загружено изображение: {img_name}'))

        self.stdout.write(
            self
            .style
            .SUCCESS(f'Место "{place.title}" загружено полностью!'))
