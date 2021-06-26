from django import forms
from .models import Host
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from localflavor.us.forms import USStateSelect

class HostForm(forms.ModelForm):
    
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
            'image1',
            'image2',
            'image3',
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
            'image1',
            'image2',
            'image3',
        ]
        widgets = {
          'start_date'  : forms.SelectDateWidget,
          'end_date'    : forms.SelectDateWidget,
          'state'       : USStateSelect(),
          'availability': forms.Textarea(attrs={'rows':3, 'cols':15}),
          'notes'       : forms.Textarea(attrs={'rows':3, 'cols':15}),
        }


