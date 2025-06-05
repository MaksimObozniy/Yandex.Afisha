from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from places.views import render_map_page, place_detail, place_title
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_map_page),
    path('places/<int:place_id>/', place_detail),
    path('tinymce/', include('tinymce.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)