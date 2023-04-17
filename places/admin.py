from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    raw_id_fields = ("place",)
    readonly_fields = ["place_image"]

    def place_image(self, obj):
        return format_html(
            '<img src="{}" style="max-width:{};max-height:{};width:{};height:{};" />',
            obj.image.url,
            "200px",
            "200px",
            "auto",
            "auto",
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ["title"]
    inlines = [ImageInline]
    search_fields = ["title"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["image"]
