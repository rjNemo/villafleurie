from django import forms
from rental.models.contact import Contact
from rental.models.place import Place


class ContactForm(forms.Form):

    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': 'Nom *'
        }),
        required=True,
    )

    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': 'Email *'
        }),
        required=True,
    )

    subject = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': 'Sujet *'
        }),
        required=True,
    )

    message = forms.CharField(
        label='',
        # max_length=100,
        min_length=4,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'cols': '45',
            'rows': '8',
            'placeholder': 'Message *'
        }),
        required=True
    )
