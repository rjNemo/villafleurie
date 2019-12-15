from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Testimonial, Reservation, Guest, Place
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .forms import ReservationForm, ContactForm
from django.db import IntegrityError
from rental.pricing import get_reservation_price
from rental.bookings import check_availability, synchronize_calendars, update_calendar
from rental.mailing import send_confirmation_mail, send_notification, send_quotation


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
    images = []
    for place in places:
        imgs = place.images.all()
        images.append(imgs)
    context = {
        'places': places,
        'images': images
    }
    return render(request, 'rental/list_place.html', context)


def location(request, place_name='T2'):
    place = get_object_or_404(Place, name=place_name)
    images = place.images.all()
    context = {
        'place': place,
        'images': images
    }
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
                if available:
                    price = get_reservation_price(place, start, end)
                    reservation = Reservation.objects.create(
                        guest=guest,
                        place=place,
                        message=message,
                        start=start,
                        end=end,
                        price=price
                    )
                    context = {
                        'reservation': reservation
                    }
                    return render(request, 'rental/merci.html', context)
                else:
                    context = {'form': form}
                    return render(request, 'rental/reservation.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. \
                Merci de recommencer votre requête."
    else:
        form = ReservationForm()
    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'rental/detail_place.html', context)


def reservation(request):
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
                    send_quotation(reservation)
                    update_calendar(reservation)
                    context = {
                        'reservation': reservation
                    }

                    return render(request, 'rental/merci.html', context)
                else:
                    context = {'form': form}
                    return render(request, 'rental/reservation.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."
    else:
        form = ReservationForm()
    context = {'form': form}
    context['errors'] = form.errors.items()
    return render(request, 'rental/reservation.html', context)


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
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_confirmation_mail(name, email)
            send_notification(subject, name, message)
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
