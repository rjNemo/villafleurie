from datetime import datetime

from django.shortcuts import get_object_or_404
from django.test import TestCase

from rental.models.booking import Booking
from rental.models.guest import Guest
from rental.models.place import Place


class BookingTestCase(TestCase):
    def setUp(self):
        self.place = Place.objects.create(
            name='TX',
            price=100
        )

        self.guest = Guest.objects.create(
            name="Ruidy",
            email="r@mail.com",
            phone="1092198YE8939798"
        )

        self.start = datetime(2019, 11, 14)
        self.end = datetime(2019, 11, 20)

    def test_BookingPrice(self):
        booking = Booking.objects.create_booking(
            place=self.place,
            start=self.start,
            end=self.end,
            guest=self.guest
        )

        self.assertEqual(booking.price, 600)
