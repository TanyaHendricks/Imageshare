from django.shortcuts import render
from .models import Album, Image, Metadata
from .forms import ImageForm, MetadataForm

import datetime

# Create your views here.
def gallery(request):
    albums = Album.objects.all() 
    images = Image.objects.all() 
    context = {
        'albums': albums,
        'images': images}        
    return render(request, 'photos/gallery.html', context)

def view_photo(request, pk):
    image = Image.objects.get(id=pk) 
    metadatas = Metadata.objects.get(image_id=pk)
    metadata_tags = metadatas.tags.all()
    context = {
        'image': image,
        'metadata_tags': metadata_tags}    
    return render(request, 'photos/photo.html', context)  

def add_photo(request):
    image_form = ImageForm()
    metadata_form = MetadataForm()
    context = {
        'image_form': image_form,
        'metadata_form': metadata_form}                         
    return render(request, "photos/photo_form.html", context)
