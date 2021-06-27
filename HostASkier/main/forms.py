from django import forms
from localflavor.us.forms import USStateSelect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class StateForm(forms.Form):
    state           = forms.CharField(widget=USStateSelect)
    enable_filter   = forms.BooleanField(required=False, label="Enable Filter")
