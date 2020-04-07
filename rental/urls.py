from django.urls import path
from . import views
from villafleurie import settings
from rental.models.booking import Booking
from rental.models.contact import Contact
from rental.models.guest import Guest
from rental.models.picture import Picture
from rental.models.place import Place
from rental.models.testimonial import Testimonial
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'rental'

urlpatterns = [
    path('', views.index, name='index'),
    path('hebergements/', views.liste_location, name='list_place'),
    path('<place_name>/', views.location, name='detail_place'),
    path('calendar/<place_name>/', views.calendar, name='calendar')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
