from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountRegisterForm
from django.contrib import messages
from urllib.parse import urlencode
import yaml
import requests 
from django.contrib.auth.decorators import login_required
from .models import Account


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

@login_required
def profile(request):

    # create an instance of a user update form
    # and a profile update form
    if request.method == 'POST':
        # u_form = AccountUpdateForm(request.POST, instance=request.user)
        # p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # if u_form.is_valid() and p_form.is_valid():
        #     u_form.save()
        #     p_form.save()
        #     messages.success(request, 'changes updated successfully')
        pass
    else:
        pass
        # u_form = AccountUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)
    # pass both forms into render as a context dictionary
    context = {
        'u_form': []
    }
    return render(request, 'account/profile.html', context)

@login_required
def pending_coordinators_view(request):
    if request.user.is_admin:
        context = {
            'pending_coordinators' : Account.objects.filter(approved=False)
        }
        return render(request, "account/pending_coordinators.html", context)
    else:
        context = {
            'data' : []
        }
        return render(request, "main/not_approved_admin.html", context)