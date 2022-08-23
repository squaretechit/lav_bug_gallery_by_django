from django.shortcuts import render, get_object_or_404
from .models import CreateGallery, GalleryImage


class LuvBugGallery:

    def gallery(self):
        context = {
            'galleries': CreateGallery.objects.all()
        }
        return render(self, 'galllery.html', context)

    def single_gallery(self, url):
        gallery_id = get_object_or_404(CreateGallery, url=url)
        context = {
            'gallery_name': gallery_id.title,
            'images': GalleryImage.objects.filter(gallery=gallery_id)
        }
        return render(self, 'single-galllery.html', context)
