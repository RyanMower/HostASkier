from django import forms
from .models import Skier
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from localflavor.us.forms import USStateSelect

class SkierForm(forms.ModelForm):

    start_date  = forms.DateField(widget=forms.SelectDateWidget)
    end_date    = forms.DateField(widget=forms.SelectDateWidget)

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
            Row(
                Column('city', css_class='form-group col-md-4 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('university', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('events', css_class='form-group col-md-4 mb-0'),
                Column('start_date', css_class='form-group col-md-4 mb-0'),
                Column('end_date', css_class="form-group col-md-4 mb-0"),
                css_class='form-row'
            ),
            'availability',
            Submit('submit', 'Submit')
        )


    class Meta:
        model = Skier
        fields = [
            'name',
            'email',
            'phone_number',
            'city',
            'state',
            'events',
            'availability',
            'start_date',
            'end_date',
            'university',
        ]
        widgets = {
          'availability': forms.Textarea(attrs={'rows':3, 'cols':15}),
          'state': USStateSelect(),
        }


