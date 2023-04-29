import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = "Load place meta from JSON to DB"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str, help="JSON file URL")

    def fetch_imgs(self, place, links):
        for number, link in enumerate(links):
            response = requests.get(link)
            response.raise_for_status()
            path, ext = os.path.splitext(link)
            img = ContentFile(
                response.content,
                name=f"{place.title}_{number}{ext}",
            )
            Image.objects.create(place=place, image=img, order=number)

    def handle(self, *args, **options):
        url = options["url"]
        response = requests.get(url)
        response.raise_for_status()
        place_meta = response.json()
        img_links = place_meta["imgs"]

        place, created = Place.objects.get_or_create(
            title=place_meta["title"],
            defaults={
                "description_short": place_meta.get("description_short"),
                "description_long": place_meta.get("description_long"),
                "lon": place_meta["coordinates"]["lng"],
                "lat": place_meta["coordinates"]["lat"],
            },
        )

        if not created:
            return

        self.fetch_imgs(place, img_links)
