from django.contrib import admin
from .models import Testimonial, Reservation, Guest, Place, Image, Contact


admin.site.register(Contact)
admin.site.register(Guest)
admin.site.register(Image)
admin.site.register(Place)
admin.site.register(Reservation)
admin.site.register(Testimonial)
