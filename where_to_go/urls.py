from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from places.views import render_map_page, place_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_map_page),
    path('places/<int:place_id>/', place_detail),
    path('tinymce/', include('tinymce.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT
                          )
