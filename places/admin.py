from django.contrib import admin

from .models import Place, PlaceImage
# Register your models here.

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ['image', 'order'] 


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ['__str__']