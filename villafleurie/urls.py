from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # change admin path for security purposes
    path('dashboard/', admin.site.urls),
    path('', include('rental.urls', namespace='rental'))
]

handler500 = 'rental.views.errors.handler500'
handler404 = 'rental.views.errors.handler404'
