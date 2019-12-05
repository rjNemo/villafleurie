from rental.models import Reservation

def get_bookings(place):
    """
    returns a list of all related place reservations
    """
    booked_dates = Reservation.objects.all()
    return [booking for booking in booked_dates if booking.place.name == f"{place.name}"]


def check_availability(place, start_date, end_date):
    """
    check if the related place is available during a given period
    """
    bookings = get_bookings(place)
    for booking in bookings:
        if (booking.start <= start_date <= booking.end) or (booking.start <= end_date <= booking.end):
            return False
    return True
