from django.db import models
import uuid

# Create your models here.
 
class Image(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    album_id = models.ForeignKey('Album', on_delete=models.RESTRICT, null=False, blank=False, default="Unknown")
    image = models.ImageField(null=False, blank=False, default="")
    description = models.TextField(null=False, blank=False, default="Unknown")
    def __str__(self):
        return self.description

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False, default="Unknown", unique=True)
    def __str__(self):
        return self.name

class Capturer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    alias = models.CharField(max_length=20, null=False, blank=False, unique=True)
    name = models.CharField(max_length=20, null=False, blank=False)
    surname = models.CharField(max_length=20, null=False, blank=False)
    def __str__(self):
        return self.alias 

class Metadata(models.Model):
    image_id = models.OneToOneField(Image, on_delete=models.CASCADE, null=False, blank=False)
    geolocation_latitude = models.DecimalField(max_digits=8, decimal_places=6, 
        null=False, blank=False)
    geolocation_longitude = models.DecimalField(max_digits=9, decimal_places=6,
        null=False, blank=False)
    captured_date = models.DateTimeField(null=False, blank=False)
    capturer_id = models.ForeignKey(Capturer, on_delete=models.RESTRICT)
    tags = models.ManyToManyField(Tag, blank=False, default="Unknown")
    def __str__(self):
        return str(self.image_id)

class Album(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=20, null=False, blank=False, default="Unknown", unique=True)
    def __str__(self):
        return self.name



