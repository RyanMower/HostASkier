from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountRegisterForm
from django.contrib import messages
from urllib.parse import urlencode
import yaml
import requests 




def register(request):

    # determines whether the form is being submitted or visited
    # is a POST request when being submitted
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)

        # check validity of form
        if form.is_valid():

            # saves user
            form.save()

    else:
        form = AccountRegisterForm()
    return render(request, 'account/register.html', {'form':form})
