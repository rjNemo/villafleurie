from django.contrib import admin
from rental.models.booking import Booking
from rental.models.contact import Contact
from rental.models.guest import Guest
from rental.models.picture import Picture
from rental.models.place import Place
from rental.models.testimonial import Testimonial


admin.site.register(Booking)
admin.site.register(Guest)
admin.site.register(Place)
admin.site.register(Contact)
admin.site.register(Picture)
admin.site.register(Testimonial)
