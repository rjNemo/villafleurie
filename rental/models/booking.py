from datetime import datetime
from django.db import models
from rental.models.guest import Guest
from rental.models.place import Place
import rental.services.calendar as calendar


class BookingManager(models.Manager):
    """ BookingManager is the interface through which database query operations
        are provided to Django models.
    """

    def create_booking(self, **kwargs):
        """ create_booking creates a Booking instance, computes the price and 
            updates the remote calendar. """
        booking = self.create(**kwargs)
        booking.price = booking.get_price()
        calendar.update(booking)
        return booking


class Booking(models.Model):
    class Meta:
        verbose_name = 'Réservation'

    def __str__(self):
        return "Réservation du {} par {}".format(self.place, self.guest)

    objects = BookingManager()

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    start = models.DateField()
    end = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def get_price(self):
        """ Compute booking price as a function of place and dates """

        if type(self.start) == str:
            self.start = datetime.strptime(self.start, '%Y-%m-%d')
        if type(self.end) == str:
            self.end = datetime.strptime(self.end, '%Y-%m-%d')
        nights = (self.end - self.start).days

        return self.place.price * nights
