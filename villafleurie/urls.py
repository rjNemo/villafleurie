from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from rental import views
# from django.contrib.flatpages import views as flat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('a-propos/', views.about, name='about'),
    path('reservation/', views.Reserver.as_view(), name='reservation'),
    path('', include('rental.urls', namespace='rental')),
]
