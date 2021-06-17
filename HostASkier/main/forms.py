from django import forms
from .models import Host, Skier

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = [
            'name',
            'email',
            'phone_number',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'events',
            'availability',
            'notes',
        ]

class SkierForm(forms.ModelForm):
    class Meta:
        model = Skier
        fields = [
            'name',
            'email',
            'phone_number',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'events',
            'availability',
            'start_date',
            'end_date'
        ]

