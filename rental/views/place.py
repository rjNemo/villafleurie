from django.shortcuts import get_object_or_404, render

from rental.models.place import Place
from rental.models.testimonial import Testimonial
from rental.views.booking import handle_booking_form


def index(request):
    """Display homePage."""
    places = Place.objects.all()
    temoignages = Testimonial.objects.all()

    context = {
        'places': places,
        'temoignages': temoignages
    }

    return render(request, 'rental/index.html', context)


def all(request):
    """Handle places list page."""
    places = Place.objects.all()

    context = {'places': places}

    return render(request, 'rental/list_place.html', context)


def view(request, place_name='T2'):
    """Handle a specific place."""
    place = get_object_or_404(Place, name=place_name)
    images = place.images.all()

    context = {
        'place': place,
        'images': images
    }

    context, template = handle_booking_form(
        request, context, init_template='rental/detail_place.html')

    return render(request, template, context)
