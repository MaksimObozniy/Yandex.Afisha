from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


def return_html(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', return_html),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)