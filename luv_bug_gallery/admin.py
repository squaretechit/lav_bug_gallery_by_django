from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CreateGallery, GalleryImage


admin.site.site_header = 'Luv Bug admin Dashboard'
admin.site.site_title = 'Luv Bug'
admin.site.index_title = 'Luv Bug Administration'

admin.site.unregister(Group)

@admin.register(CreateGallery)
class CreateGalleryAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'image')
    fields = ('title', 'image')

@admin.register(GalleryImage)
class GalleryImagesAdmin(admin.ModelAdmin):
    list_display = ('date', 'gallery', 'title', 'image')
    # fields = ('date', 'title', 'image')
