from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rental.urls', namespace='rental'))
]

handler500 = 'rental.views.errors.handler500'
handler404 = 'rental.views.errors.handler404'
