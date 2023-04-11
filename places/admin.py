from django.contrib import admin

from .models import Image, Place


class ImageInline(admin.TabularInline):
    model = Image
    raw_id_fields = ("place", )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines = [ImageInline]

admin.site.register(Image)
