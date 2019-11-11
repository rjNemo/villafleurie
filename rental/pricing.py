"""
Compute booking price as a function of place and dates
"""
from models import Place
from datetime import *
from django.shortcuts import get_object_or_404

place_name = 'T2'
start = datetime(2019, 11, 14)
end = datetime(2019, 11, 20)

stay = end-start
nights = stay.days

def quotation(place_name, nights):
    place = get_object_or_404(Place, name=place_name)
    return place.price_per_night * (end - start)

x = quotation(place_name, nights)
print(x)
