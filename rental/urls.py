from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path
from villafleurie import settings
from rental.views import home, views


app_name = 'rental'

urlpatterns = [
    path('a-propos/', home.About.as_view(), name='about'),
    path('legal/', home.Legal.as_view(), name='legal'),
    path('partenaires/', home.Partners.as_view(), name='partners'),
    path('services/', home.Services.as_view(), name='services'),

    path('contact/', views.contact, name='contact'),
    path('reservation/', views.reservation, name='reservation'),

    path('', views.index, name='index'),
    path('hebergements/', views.liste_location, name='list_place'),
    path('<place_name>/', views.location, name='detail_place'),
    # path('calendar/<place_name>/', views.calendar, name='calendar'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
