""" URLs specifi to rental application """

from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path

from rental.views import booking, contact, home, place
from villafleurie import settings

app_name = 'rental'

urlpatterns = [
    path('a-propos/', home.About.as_view(), name='about'),
    path('legal/', home.Legal.as_view(), name='legal'),
    path('partenaires/', home.Partners.as_view(), name='partners'),
    path('services/', home.Services.as_view(), name='services'),

    path('contact/', contact.view, name='contact'),

    path('reservation/', booking.view, name='reservation'),
    path('paiement/', booking.pay, name='payment'),

    path('', place.index, name='index'),
    path('hebergements/', place.all, name='list_place'),
    path('<slug:place_name>/', place.view, name='detail_place')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
