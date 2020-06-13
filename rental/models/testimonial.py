from django.db import models

from rental.models.booking import Booking
from rental.models.guest import Guest


class Testimonial(models.Model):
    class Meta:
        verbose_name = "Témoignage"

    def __str__(self):
        return f"Témoignage de {self.author}"

    author = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    picture = models.ImageField(
        max_length=200, upload_to='img/', null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    guest = models.OneToOneField(
        Guest, on_delete=models.CASCADE, blank=True, null=True)
    reservation = models.OneToOneField(
        Booking, on_delete=models.CASCADE, blank=True, null=True)
