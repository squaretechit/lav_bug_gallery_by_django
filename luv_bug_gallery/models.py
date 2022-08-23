from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class CreateGallery(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    url = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to="create_gallery_images")

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.title + '-' + get_random_string(length=4))
        else:
            self.url = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/gallery/{self.url}/'
    def __str__(self):
        return str(self.title)


class GalleryImage(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    gallery = models.ForeignKey(CreateGallery, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery_images")

    def __str__(self):
        return str(self.title)
