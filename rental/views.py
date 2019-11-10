from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Testimonial, Reservation, Guest, Place
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from.forms import ReservationForm
from django.db import IntegrityError


# class Accueil(ListView):
#     model = Place
#     template_name = 'rental/index.html'
#     context_object_name = 'places'

def index(request):
    places = Place.objects.all()
    temoignages = Testimonial.objects.all()
    context = {
        'places' : places,
        'temoignages' : temoignages
    }
    return render(request, 'rental/index.html', context)


def liste_location(request):
    places = Place.objects.all()
    images = []
    for place in places:
        imgs = place.images.all()
        images.append(imgs)
    context = {
        'places' : places,
        'images' : images
    }
    return render(request, 'rental/list_place.html', context)

# class ListeLocation(ListView):
#     model = Place
#     template_name = 'rental/list_place.html'
#     context_object_name = 'places'


def location(request, place_name='T2'):
    place = get_object_or_404(Place, name=place_name)
    images = place.images.all()
    context = {
        'place' : place,
        'images' : images
    }
    if request.method == 'POST':
        form = ReservationForm(request.POST)#, error_class=ParagraphErrorList)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            place_name = form.cleaned_data['place']
            try:
                guest = Guest.objects.filter(email=email)
                if not guest.exists():
                    guest = Guest.objects.create(
                        email=email,
                        name=name
                    )
                else:
                    guest = guest.first()

                place = get_object_or_404(Place, name=place_name)
                reservation = Reservation.objects.create(
                    guest=guest,
                    place=place,
                    message=message
                )
                context = {
                    'guest': guest,
                    'place': place
                }
                return render(request, 'rental/merci.html', context)
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
        form = ReservationForm(request.POST)#, error_class=ParagraphErrorList)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            place_name = form.cleaned_data['place']
            try:
                guest = Guest.objects.filter(email=email)
                if not guest.exists():
                    guest = Guest.objects.create(
                        email=email,
                        name=name
                    )
                else:
                    guest = guest.first()
                place = get_object_or_404(Place, name=place_name)
                reservation = Reservation.objects.create(
                    guest=guest,
                    place=place,
                    message=message
                )
                context = {
                    'guest': guest,
                    'place': place
                }
                return render(request, 'rental/merci.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."
    else:
        form = ReservationForm()
    context = {'form' : form}
    context['errors'] = form.errors.items()
    return render(request, 'rental/reservation.html', context)


class Contact(TemplateView):
    template_name = 'rental/contact.html'


class Legal(TemplateView):
    template_name = 'rental/legal.html'


class About(TemplateView):
    template_name = 'rental/about.html'


# class Merci(TemplateView):
#     template_name = 'rental/merci.html'


def handler404(request, exception):
    return render(request, 'store/404.html', status=404)


def handler500(request):
    return render(request, 'store/500.html', status=500)
