from django.shortcuts import render
from .models import Album, Image, Metadata

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
    return render(request, 'photos/photo.html', {'image': image})  

def add_photo(request):
    return render(request, 'photos/add.html')  
