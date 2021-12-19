
from django.contrib import admin

# Register your models here.
from .models import Image
from .models import Tag
from .models import Metadata
from .models import Album


admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Metadata)
admin.site.register(Album)


