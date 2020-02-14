from django.db import models

# Create your models here.
class Navigation(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='vehicles')
    datetime = models.DateTimeField(verbose_name='Tarih', auto_now_add=True)
    latitude = models.FloatField(max_length=120, verbose_name='Enlem')
    longitude = models.FloatField(max_length=120, verbose_name='Boylam')

class Vehicle(models.Model):
    plate = models.CharField(max_length=200, verbose_name='Plaka')

    def __str__(self):
        return self.plate
        
    class Meta:
        ordering = ['id']