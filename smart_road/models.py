from django.db import models

# Create your models here.


class Event(models.Model):
    event_id = models.IntegerField(null=True)
    cell_name = models.CharField(max_length=300)

