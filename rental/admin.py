from django.contrib import admin
from .models import Testimonial, Reservation, Guest, Place, Image


admin.site.register(Place)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Testimonial)
admin.site.register(Image)
