from django.shortcuts import render

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
                "detailsUrl": detail_urls[place.id - 1],
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
