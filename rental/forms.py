from django import forms
from .models import Reservation, Place, Guest
from .enums import PlaceNames


class ReservationForm(forms.Form):

    name = forms.CharField(
        label="",
        max_length=100,
        min_length=4,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': 'Nom *'
        }),
        required=True)

    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': 'Email *'
        }),
        required=True
    )

    phone = forms.CharField(
        label='',
        max_length=30,
        min_length=4,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': 'Téléphone *'
        }),
        required=True)

    place = forms.ChoiceField(
        label='',
        widget=forms.Select(
            attrs={'class': 'form-control form-control-lg form-control-a'}),
        required=True,
        choices=PlacesNames.choices,
        default=PlacesNames.T2
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
        required=True)

    start = forms.DateField(
        label='',
        input_formats=['%d/%m/%Y'],
        # max_length=100,
        # min_length=4,
        widget=forms.DateInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': '01/01/2020 *'}),
        required=True)

    end = forms.DateField(
        label='',
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': '31/12/2020 *'}),
        required=True)


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
