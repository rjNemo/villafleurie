from datetime import datetime

from django.db import models

import rental.services.calendar as calendar
import rental.tasks.api_mailer as mailer  # or g_mailer
from rental.models.guest import Guest
from rental.models.place import Place


class BookingManager(models.Manager):
    """
    BookingManager is the interface through which database query operations
    are provided to Django models.
    """

    def create_booking(self, **kwargs):
        """
        Create_booking creates a Booking instance, computes the price and
        updates the remote calendar.
        """

        booking = self.create(**kwargs)
        booking.price = booking.get_price()
        calendar.update(booking)

        return booking


class Booking(models.Model):
    """ Booking encapsulate booking instance information """

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
        """ Compute booking price as a function of place and dates. """

        if isinstance(self.start, str):
            self.start = datetime.strptime(self.start, '%Y-%m-%d')
        if isinstance(self.end, str):
            self.end = datetime.strptime(self.end, '%Y-%m-%d')
        nights = (self.end - self.start).days

        return self.place.price * nights

    def send_quotation(self):
        """ Notify user of booking details """

        mailer.send_quotation.delay(self.guest.name, self.guest.email)
