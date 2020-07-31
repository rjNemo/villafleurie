from django.shortcuts import render

from rental.forms.contact import ContactForm
from rental.models.contact import Contact


def view(request):
    """
    Handle contact form submission after validation and redirect to success page.
    """

    # create blank form or populates fields using post request data
    form = ContactForm(
        request.POST) if request.method == 'POST' else ContactForm()

    # simply display contact page, persist form values in case of errors
    if request.method == 'GET' or not form.is_valid():
        return render(request, 'rental/contact.html', {'form': form})

    # create contact object to db
    contact = Contact.objects.create(
        name=form.cleaned_data['name'],
        email=form.cleaned_data['email'],
        subject=form.cleaned_data['subject'],
        message=form.cleaned_data['message']
    )

    # handle messaging
    contact.send_confirmation()
    contact.send_notification()

    # redirect to success page
    return render(request, 'rental/contact_merci.html', {})
