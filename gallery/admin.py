from django.contrib import admin
from gallery.models import Gallery
# Register your models here.
class GalleryData(admin.ModelAdmin):
    list_display=['Gallery_img']
    ordering=('id',)
admin.site.register(Gallery,GalleryData)