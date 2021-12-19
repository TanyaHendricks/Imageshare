from django.shortcuts import redirect, render
from .models import Album, Image, Metadata
from .forms import ImageForm, MetadataForm
from django.contrib.auth.decorators import login_required


def view_gallery(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    album = Album.objects.filter(name__icontains=search_query)
    images = Image.objects.filter(album_id__in=(album.values_list('id', flat=True)))
 
    context = {
        'albums': album,
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


@login_required(login_url="login")
def add_photo(request):
    profile = request.user.profile
    image_form = ImageForm()
    metadata_form = MetadataForm()

    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            metadata_form.image_id = image.id
            image.owner = profile
            image_form.save()
                    
    if request.method == 'POST':
        metadata_form = MetadataForm(request.POST)
        if metadata_form.is_valid():
            metadata_form.save()
            return redirect('add_photo')

    context = {
        'image_form': image_form,
        'metadata_form': metadata_form}
    return render(request, 'photos/photo_form.html', context)


@login_required(login_url="login")
def update_photo(request, pk):
    image = Image.objects.get(id=pk)
    image_form = ImageForm(instance=image)

    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES, instance=image)
        if image_form.is_valid():
            image_form.save()
            return redirect('add_photo')

    metadata = Metadata.objects.get(image_id=pk)
    metadata_form = MetadataForm(instance=metadata)

    if request.method == 'POST':
        metadata_form = MetadataForm(request.POST, instance=metadata)
        if metadata_form.is_valid():
            metadata_form.save()
            return redirect('add_photo')

    context = {
        'image_form': image_form,
        'metadata_form': metadata_form}
    return render(request, 'photos/photo_form.html', context)


@login_required(login_url="login")
def delete_photo(request, pk):
    image = Image.objects.get(id=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery')
    context = {'object': image}
    return render(request, 'photos/delete_template.html', context)
