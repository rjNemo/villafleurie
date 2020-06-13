from django.db import models

from rental.models.picture import Picture
import rental.services.calendar as calendar


class Place(models.Model):
    class Meta:
        verbose_name = "Appartement"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    info = models.TextField(blank=True)
    subname = models.CharField(max_length=100, blank=True)
    tagline = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    surface = models.IntegerField(null=True, blank=True)
    beds = models.IntegerField(null=True, blank=True)
    max_occupation = models.IntegerField(null=True, blank=True)
    thumbnail = models.ForeignKey(
        Picture, on_delete=models.CASCADE, blank=True, null=True)
    images = models.ManyToManyField(Picture, related_name="places", blank=True)
    calendar = models.CharField(max_length=350, blank=True, null=True)

    def is_available(self, start, end):
        return calendar.check_availability(self, start, end)
