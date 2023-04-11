from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def render_main(request):
    features = []
    detail_urls = ["static/places/moscow_legends.json", "static/places/roofs24.json"]
    places = Place.objects.all()

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [place.lon, place.lat]},
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse("place_meta", args=(place.id, )),
            },
        }
        features.append(feature)

    context = {
        "places": {
            "type": "FeatureCollection",
            "features": features,
        }
    }

    return render(request, "index.html", context)


def get_place_meta(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    context = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }
    return JsonResponse(
        context,
        json_dumps_params={"ensure_ascii": False, "indent": 4}
    )
