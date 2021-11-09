from django.contrib import admin

# Register your models here.
from .models import Image
from .models import MetaData
from .models import Tag

admin.site.register(Image)
admin.site.register(MetaData)
admin.site.register(Tag)