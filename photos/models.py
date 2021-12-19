from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from users.models import Profile

# Create your models here.


class Image(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    album_id = models.ForeignKey(
        'Album', on_delete=models.RESTRICT, null=False, blank=False, default="Unknown")
    image = models.ImageField(null=False, blank=False, default="default.jpg")
    description = models.TextField(unique=True,null=False, blank=False, default="None")

    def __str__(self):
        return self.description


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=False,
                            blank=False, default="None", unique=True)

    def __str__(self):
        return self.name



class Metadata(models.Model):
    image_id = models.OneToOneField(
        Image, on_delete=models.CASCADE, null=False, blank=False)
    geolocation_latitude = models.DecimalField(max_digits=8, decimal_places=6,
                                               null=False, blank=False)
    geolocation_longitude = models.DecimalField(max_digits=9, decimal_places=6,
                                                null=False, blank=False)
    captured_date = models.DateTimeField(null=False, blank=False)
    tags = models.ManyToManyField(Tag, blank=False, default="None")

    def __str__(self):
        return str(self.image_id)


class Album(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=20, null=False,
                            blank=False, default="None", unique=True)

    def __str__(self):
        return self.name
