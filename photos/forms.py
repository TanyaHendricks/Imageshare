from django.forms import ModelForm
from .models import Image, Metadata

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

class MetadataForm(ModelForm):
    class Meta:
        model = Metadata
        fields = '__all__'

    
