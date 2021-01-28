from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _

from rental.forms.booking import BookingForm
from rental.models.booking import Booking
from rental.models.guest import Guest
from rental.models.place import Place
import stripe

def pay(request):
    if request.method == 'GET':
        return render(request, 'rental/pay.html', {})

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "eur",
                    "product_data": {"name": "Nassira Basmaison: Réservation du 28/01/2021 au 8/02/2021"},
                    "unit_amount": 91300,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="http://villafleuriegp.com/",
        cancel_url="http://villafleuriegp.com/paiement",
    )

    return {"id": session.id}

def view(request):
    """Return initial booking form."""
    context, template = handle_booking_form(request)

    return render(request, template, context)


def handle_booking_form(request, context=None, init_template='rental/reservation.html'):
    """
    Validates booking form and checks place availability for a given period.
    Returns the context and the template to be rendered.
    """

    if not context:
        context = {}

    # create form and populate fields using post request data
    form = BookingForm(
        request.POST) if request.method == 'POST' else BookingForm()

    # return is form is not valid, persist already inputed data
    if not form.is_valid():
        context['form'] = form
        return context, init_template

    # parse request data
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    phone = form.cleaned_data['phone']
    message = form.cleaned_data['message']
    place_name = form.cleaned_data['place']
    start = form.cleaned_data['start']
    end = form.cleaned_data['end']

    # get guest
    guest = Guest.objects.filter(email=email)
    if guest.exists():
        guest = guest.first()
    else:
        guest = Guest.objects.create(
            email=email,
            name=name,
            phone=phone
        )

    # check place availability
    place = get_object_or_404(Place, name=place_name)

    if not place.is_available(start, end):
        form.add_error(None, ValidationError(
            _("Cet hébergement n'est pas disponible aux dates indiquées."),
            code='invalid'
        ))
        return {'form': form}, 'rental/reservation.html'

    reservation = Booking.objects.create_booking(
        guest=guest,
        place=place,
        message=message,
        start=start,
        end=end
    )

    reservation.send_quotation()
    context['reservation'] = reservation

    return context, 'rental/merci.html'
