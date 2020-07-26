from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _

from rental.forms.booking import BookingForm
from rental.models.booking import Booking
from rental.models.guest import Guest
from rental.models.place import Place


def view(request):
    context, template = handle_booking_form(request)

    return render(request, template, context)


def handle_booking_form(request, context={}, init_template='rental/reservation.html'):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            place_name = form.cleaned_data['place']
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']

            try:
                guest = Guest.objects.filter(email=email)
                if not guest.exists():
                    guest = Guest.objects.create(
                        email=email,
                        name=name,
                        phone=phone
                    )
                else:
                    guest = guest.first()

                place = get_object_or_404(Place, name=place_name)

                if place.is_available(start, end):
                    reservation = Booking.objects.create_booking(
                        guest=guest,
                        place=place,
                        message=message,
                        start=start,
                        end=end
                    )

                    reservation.send_quotation()

                    context = {
                        'reservation': reservation
                    }
                    template = 'rental/merci.html'
                    return context, template
                else:
                    form.add_error(None,  ValidationError(
                        _("Cet hébergement n'est pas disponible aux dates indiquées."),
                        code='invalid'
                    ))
                    context = {'form': form}
                    template = 'rental/reservation.html'
                    return context, template

            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."
    else:
        form = BookingForm()

    context['form'] = form
    context['errors'] = form.errors.items()
    template = init_template

    return context, template
