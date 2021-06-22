from django import forms
from .models import Host
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class HostForm(forms.ModelForm):

    start_date  = forms.DateField(widget=forms.SelectDateWidget)
    end_date    = forms.DateField(widget=forms.SelectDateWidget)
    image       = forms.ImageField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('phone_number', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('events', css_class='form-group col-md-4 mb-0'),
                Column('start_date', css_class='form-group col-md-4 mb-0'),
                Column('end_date', css_class="form-group col-md-4 mb-0"),
                css_class='form-row'
            ),
            'availability',
            'notes',
            'image',
            Submit('submit', 'Submit')
        )

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
            'start_date',
            'end_date',
            'image',
        ]
