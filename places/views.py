from django.shortcuts import render, get_object_or_404
from .models import Place
import json
from django.http import JsonResponse, HttpResponse, Http404


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
                'detailsUrl': f'/places/{place.id}'
            }
        })

    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }

    context = {
        'places_geojson': json.dumps(geojson, ensure_ascii=False)
    }

    return render(request, 'index.html', context)


def place_detail(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        raise Http404('Place not found')

    return JsonResponse({
        'title': place.title,
        'imgs': [img.image.url for img in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
    }, json_dumps_params={'ensure_ascii': False, 'indent': 2})
