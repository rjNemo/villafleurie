from django.contrib import admin
from .models import Testimonial, Reservation, Guest, Place


admin.site.register(Place)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Testimonial)
