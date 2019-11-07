from django import forms
from .models import Reservation, Place, Guest
from phonenumber_field.modelfields import PhoneNumberField


class ReservationForm(forms.Form):
    PLACES=(('T2','T2'), ('T3','T3'),)
    name = forms.CharField(
        label="",
        max_length=100,
        min_length=4,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-a', 'placeholder': 'Nom *'}),
        required=True)
    email = forms.EmailField(
        label = '',
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg form-control-a', 'placeholder': 'Email *'}),
        required=True
    )
    phone = forms.CharField(
        label='',
        max_length=100,
        min_length=4,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-a', 'placeholder': 'Téléphone *'}),
        required=True)
    place = forms.ChoiceField(
        label = '',
        widget=forms.Select(attrs={'class': 'form-control form-control-lg form-control-a'}),
        required=True,
        choices=PLACES)
    message = forms.CharField(
        label='',
        max_length=100,
        min_length=4,
        widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '45', 'rows':'8', 'placeholder': 'Message *'}),
        required=True)