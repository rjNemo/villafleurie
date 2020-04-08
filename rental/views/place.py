from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from rental.models.place import Place
from rental.models.testimonial import Testimonial


def index(request):
    places = Place.objects.all()
    temoignages = Testimonial.objects.all()

    context = {
        'places': places,
        'temoignages': temoignages
    }

    return render(request, 'rental/index.html', context)


def all(request):
    places = Place.objects.all()

    context = {'places': places}

    return render(request, 'rental/list_place.html', context)


def view(request, place_name='T2'):
    place = get_object_or_404(Place, name=place_name)
    images = place.images.all()

    context = {
        'place': place,
        'images': images
    }

    context, template = handle_reservation_form(
        request, context, init_template='rental/detail_place.html')

    return render(request, template, context)
