from django.forms import ModelForm
from django.forms.fields import ChoiceField
from django.forms.models import ModelChoiceField
from .models import Album, Image, Metadata
from django import forms

class ImageForm(ModelForm):
    
    class Meta:
        model = Image
        fields = ['owner', 'album_id', 'image', 'description']
        

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['owner'].widget.attrs.update(
        #    {'class': 'input', 'placeholder': 'Select owner'})


class MetadataForm(ModelForm):
    class Meta:
        model = Metadata
        fields = ['image_id', 'geolocation_latitude',
                  'geolocation_longitude', 'captured_date', 'tags']
        widgets = {
            'captured_date': forms.SelectDateWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(MetadataForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
