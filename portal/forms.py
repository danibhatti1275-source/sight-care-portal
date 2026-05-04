from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    preferred_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label='Preferred Date'
    )

    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone', 'preferred_date', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Any notes for the doctor', 'rows': 4}),
        }
