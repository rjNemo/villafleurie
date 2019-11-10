from django.urls import path
from . import views
from villafleurie import settings
from .models import Testimonial, Reservation, Guest, Place
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'rental'

urlpatterns = [
    # path('', views.Accueil.as_view(), name='index'),
    path('', views.index, name='index'),
    path('hebergements/', views.liste_location, name='list_place'),
    # path('<place_name>/', views.Location.as_view(), name='detail_place'),
    path('<place_name>/', views.location, name='detail_place'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
