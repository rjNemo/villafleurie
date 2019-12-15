from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from rental import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('a-propos/', views.About.as_view(), name='about'),
    path('reservation/', views.reservation, name='reservation'),
    path('legal/', views.Legal.as_view(), name='legal'),
    path('partenaires/', views.Partners.as_view(), name='partners'),
    path('services/', views.Services.as_view(), name='services'),
    path('', include('rental.urls', namespace='rental')),
]

handler404 = 'rental.views.handler404'
handler500 = 'rental.views.handler500'
