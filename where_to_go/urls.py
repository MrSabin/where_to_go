from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from where_to_go import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.render_main),
    path("places/<int:place_id>/", views.get_place_meta, name="place_meta"),
    path("tinymce/", include("tinymce.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
