from datetime import datetime
from django.shortcuts import get_object_or_404
from django.test import TestCase
from rental.models.place import Place
from rental.models.booking import Booking
from rental.models.guest import Guest

place_name = 'T2'
place = get_object_or_404(Place, name=place_name)


x = get_reservation_price(place_name, start, end)
print(x)


class TestBooking(TestCase):
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

    def test_bookingPrice(self):
        # place = Place.objects.get(name='TX')
        booking = Booking.objects.create(
            place=self.place,
            start=self.start,
            end=self.end,
            guest=self.guest
        )

        self.assertEqual(booking.get_reservation_price())
