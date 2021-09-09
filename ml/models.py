from django.db import models

# Create your models here.
class PostResponse(models.Model):
  store_name=models.CharField(max_length=100)
  rider_name=models.CharField(max_length=100)
  store_delivery=models.FloatField()
  rider_store=models.FloatField()
  packaging_time=models.FloatField()
  rating=models.IntegerField()

  def __str__(self):
      return self.store_name+' '+self.rider_name
