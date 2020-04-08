from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.utils.translation import gettext_lazy as _
from rental.forms import ReservationForm, ContactForm
from rental.models.booking import Booking
from rental.models.contact import Contact
from rental.models.guest import Guest
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


def liste_location(request):
    places = Place.objects.all()

    context = {'places': places}

    return render(request, 'rental/list_place.html', context)


def location(request, place_name='T2'):
    place = get_object_or_404(Place, name=place_name)
    images = place.images.all()

    context = {
        'place': place,
        'images': images
    }

    context, template = handle_reservation_form(
        request, context, init_template='rental/detail_place.html')

    return render(request, template, context)


def reservation(request):
    context, template = handle_reservation_form(request)

    return render(request, template, context)


def handle_reservation_form(request, context={}, init_template='rental/reservation.html'):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            place_name = form.cleaned_data['place']
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']

            try:
                guest = Guest.objects.filter(email=email)
                if not guest.exists():
                    guest = Guest.objects.create(
                        email=email,
                        name=name,
                        phone=phone
                    )
                else:
                    guest = guest.first()

                place = get_object_or_404(Place, name=place_name)

                if place.is_available(start, end):
                    reservation = Booking.objects.create_booking(
                        guest=guest,
                        place=place,
                        message=message,
                        start=start,
                        end=end
                    )

                    reservation.send_quotation()

                    context = {
                        'reservation': reservation
                    }
                    template = 'rental/merci.html'
                    return context, template
                else:
                    form.add_error(None,  ValidationError(
                        _("Cet hébergement n'est pas disponible aux dates indiquées."),
                        code='invalid'
                    ))
                    context = {'form': form}
                    template = 'rental/reservation.html'
                    return context, template

            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."
    else:
        form = ReservationForm()

    context['form'] = form
    context['errors'] = form.errors.items()
    template = init_template

    return context, template


def calendar(request, place_name):
    """
    returns a list of all related place reservations
    """
    # synchronize_calendars()
    booked_dates = Booking.objects.all()
    bookings = [
        booking for booking in booked_dates if booking.place.name == place_name]
    context = {
        'place_name': place_name,
        'bookings': bookings
    }

    return render(request, 'rental/calendar.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )

            contact.send_confirmation()
            contact.send_notification()

            return render(request, 'rental/contact_merci.html', {})

    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'rental/contact.html', context)


class Legal(TemplateView):
    template_name = 'rental/legal.html'


class About(TemplateView):
    template_name = 'rental/about.html'


class Partners(TemplateView):
    template_name = 'rental/partners.html'


class Services(TemplateView):
    template_name = 'rental/service.html'


def handler404(request, exception):
    return render(request, 'rental/404.html', status=404)


def handler500(request):
    return render(request, 'rental/500.html', status=500)
