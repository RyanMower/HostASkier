from django import forms
from localflavor.us.models import USStateField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class StateForm(forms.Form):

    state  = USStateField()

    class Meta:
        fields = [
            'state',
        ]