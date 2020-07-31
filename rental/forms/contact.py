from django import forms


class ContactForm(forms.Form):
    """
    ContactForm serve to validate input and create a new contact.
    doc: https://docs.djangoproject.com/fr/2.2/topics/forms/modelforms/
    """

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
        min_length=4,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'cols': '45',
            'rows': '8',
            'placeholder': 'Message *'
        }),
        required=True
    )
