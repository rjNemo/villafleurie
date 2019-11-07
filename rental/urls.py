from django.urls import path
from . import views
from .models import Testimonial, Reservation, Guest, Place

app_name = 'rental'

urlpatterns = [
    path('', views.Accueil.as_view(), name='index'),
    path('hebergements/', views.ListeLocation.as_view(), name='list_place'),
    # path('<place_name>/', views.Location.as_view(), name='detail_place'),
    path('<place_name>/', views.location, name='detail_place'),
]
