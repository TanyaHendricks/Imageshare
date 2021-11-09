from django.db import models
import uuid

# Create your models here.

class Image(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    url = models.CharField(max_length=2000, null=False, blank=False)

class MetaData(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    geolocation_latitude = models.DecimalField(max_digits=8, decimal_places=4, 
        null=False, blank=False)
    geolocation_longitude = models.DecimalField(max_digits=9, decimal_places=4,
        null=False, blank=False)
    captured_date = models.DateTimeField(null=False, blank=False)
    captured_by = models.CharField(max_length=20, null=False, blank=False)

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    description = models.CharField(max_length=20, null=False, blank=False)

