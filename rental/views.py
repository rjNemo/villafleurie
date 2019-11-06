from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Testimonial, Reservation, Guest, Place
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


# Réservation : dans le detail_place.html ajouter un formulaire (if method = post …)
# Paiement : payer
# Remerciement après loocation
# Contact
# À propos
# Légal & CGU


class Accueil(ListView):
    model = Place
    template_name = 'rental/index.html'
    context_object_name = 'places'

class ListeLocation(ListView):
    model = Place
    template_name = 'rental/list_place.html'
    context_object_name = 'places'

class Location(DetailView):
    model = Place
    template_name = 'rental/detail_place.html'
    context_object_name = 'place'

    def get_object(self, queryset=None):
        place_name = self.kwargs.get('place_name', None)
        return get_object_or_404(Place, name=place_name)

# def location(request, place_name):
#     place = Place.objects.get(name=place_name)
#     context = {'place' : place}
#     return render(request, 'rental/detail_place.html', context)

class Contact(TemplateView):
    template_name = 'rental/contact.html'

class Reserver(TemplateView):
    template_name = 'rental/reservation.html'

def about(request):
    context = {}
    return render(request, 'rental/about.html', context)
