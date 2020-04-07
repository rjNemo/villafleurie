from datetime import datetime
from django.db import models
from rental.models.guest import Guest
from rental.models.place import Place


class Booking(models.Model):
    class Meta:
        verbose_name = 'Réservation'

    def __str__(self):
        return "Réservation du {} par {}".format(self.place, self.guest)

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    start = models.DateField()
    end = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def price(self):
        """ Compute booking price as a function of place and dates """

        if type(self.start) == str:
            self.start = datetime.strptime(self.start, '%Y-%m-%d')
        if type(self.end) == str:
            self.end = datetime.strptime(self.end, '%Y-%m-%d')
        nights = (self.end - self.start).days

        return self.place.price * nights
