from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Testimonial, Reservation, Guest, Place
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .forms import ReservationForm, ContactForm
from django.db import IntegrityError
from rental.pricing import get_reservation_price
from rental.bookings import check_availability, synchronize_calendars, update_calendar
# send_confirmation_mail, send_notification, send_quotation
from rental.tasks.apiMailer import *  # gMailer
from rental.models import Contact


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
                available = check_availability(place, start, end)
                price = get_reservation_price(place, start, end)
                if available:
                    reservation = Reservation.objects.create(
                        guest=guest,
                        place=place,
                        message=message,
                        start=start,
                        end=end,
                        price=price
                    )
                    send_quotation.delay(name, email)
                    update_calendar(reservation)
                    context = {
                        'reservation': reservation
                    }
                    template = 'rental/merci.html'
                    return context, template
                else:
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
    booked_dates = Reservation.objects.all()
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

            send_confirmation.delay(contact.name, contact.email)
            send_notification.delay(
                contact.name,
                contact.email,
                contact.subject,
                contact.message,
                contact.date
            )

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
