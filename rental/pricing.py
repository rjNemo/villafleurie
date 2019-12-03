def get_reservation_price(place, start, end):
    """
    Compute booking price as a function of place and dates
    """
    nights = (end - start).days
    return place.price * nights


if __name__ == '__main__':
    from rental.models import Place
    from datetime import *
    from django.shortcuts import get_object_or_404
    place_name = 'T2'
    place = get_object_or_404(Place, name=place_name)
    start = datetime(2019, 11, 14)
    end = datetime(2019, 11, 20)
    x = get_reservation_price(place_name, start, end)
    print(x)
