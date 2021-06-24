from django import forms
from account.models import Account
from django.contrib.auth.forms import UserCreationForm

# new class adds email field to usercreation form
class AccountRegisterForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ['email', 
                  'username',
                  'first_name',
                  'last_name',
                  'phone_number', 
                  'password1', 
                  'password2'
                  ]

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'phone_number']