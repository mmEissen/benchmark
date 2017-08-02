from django.db import models

# Create your models here.



class Item(models.Model):

    name = models.CharField(max_length=255, primary_key=True)


class Measurement(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    time_delta = models.DurationField()
