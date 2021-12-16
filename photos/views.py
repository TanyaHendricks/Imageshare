from django.shortcuts import redirect, render
from .models import Album, Image, Metadata
from .forms import ImageForm, MetadataForm


def view_gallery(request):
    if request.method == "POST":
        search_query = request.POST["search_query"]
        album = Album.objects.get(name__contains=search_query)
        images = Image.objects.filter(album_id=album.id)

    else:
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

    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            metadata_form.image_id = image.id
            image_form.save()
            return redirect('add_photo')

    if request.method == 'POST':
        metadata_form = MetadataForm(request.POST)
        if metadata_form.is_valid():
            metadata_form.save()
            return redirect('add_photo')

    context = {
        'image_form': image_form,
        'metadata_form': metadata_form}
    return render(request, 'photos/photo_form.html', context)


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


def delete_photo(request, pk):
    image = Image.objects.get(id=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery')
    context = {'object': image}
    return render(request, 'photos/delete_template.html', context)
