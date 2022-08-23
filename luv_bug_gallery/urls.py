from django.urls import path
from .views import LuvBugGallery


urlpatterns = [
    path('', LuvBugGallery.gallery, name='gallery'),
    path('gallery/<str:url>/', LuvBugGallery.single_gallery, name='single_gallery'),
]
