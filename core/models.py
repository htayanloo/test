from django.db import models

# Create your models here.
from djgeojson.fields import PolygonField
from django.db import models


class MushroomSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    geom = PolygonField()

    def __str__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture.url


class SmsStack(models.Model):
    receiver = models.IntegerField()
    message = models.CharField(max_length=100)
    status = models.SmallIntegerField(choices=((0,"در صف ارسال"),(1,"ارسال شده"),(2,"مشکل در ارسال")))



class MciArea(models.Model):
    title = models.CharField(max_length=100)
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)
