from django.urls import reverse
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Place

def place_title(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return HttpResponse(place.title)


def render_map_page(request):
    places = Place.objects.all()

    features = []
    for place in places:
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude],
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_detail', args=[place.id])
                }
        })

    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }

    context = {
        'places_geojson':geojson
    }

    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)

    return JsonResponse({
        'title': place.title,
        'imgs': [img.image.url for img in place.images.all()],
        'short_description_short': place.short_description,
        'long_description': place.long_description,
    }, json_dumps_params={'ensure_ascii': False, 'indent': 2})
