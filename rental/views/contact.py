from django.shortcuts import render
from rental.forms.contact import ContactForm
from rental.models.contact import Contact


def view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )

            contact.send_confirmation()
            contact.send_notification()

            return render(request, 'rental/contact_merci.html', {})

    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'rental/contact.html', context)
