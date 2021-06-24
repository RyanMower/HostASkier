from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountRegisterForm, AccountUpdateForm
from django.contrib import messages
from urllib.parse import urlencode
import yaml
import requests 
from django.contrib.auth.decorators import login_required
from .models import Account

# Register a coordinator
def register(request):
    # determines whether the form is being submitted or visited
    # is a POST request when being submitted
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)
        # check validity of form
        if form.is_valid():
            # saves user
            form.save()
            messages.success(request, f'{request.user.username}, you successfully created an account!')
            return render('home')

    else:
        form = AccountRegisterForm()
    return render(request, 'account/register.html', {'form':form})


@login_required
def pending_coordinators_view(request):

    if not request.user.is_admin: ## Ensure user is admin
        context = {
            'data' : []
        }
        return render(request, "main/not_approved_admin.html", context)

    if request.method == 'POST':
        # First, you should retrieve the team instance you want to update
        account = Account.objects.filter(id=request.POST['id']).first()

        # Next, you update the status
        if request.POST.get('status'):
            if request.POST.get('status') == "Accept":
                account.approved = True
                account.save()
            elif request.POST.get('status') == "Decline":
                account.delete() ## Deletes the object from the database

    pending_coordinators = Account.objects.filter(approved=False)

    ## Check if there are any pending-coordinators to render
    if len(pending_coordinators) == 0:
        context = None
        return render(request, "account/no_pending_coordinators.html", context)
    else:
        context = {
            'pending_coordinators' : pending_coordinators,
        }
        return render(request, "account/pending_coordinators.html", context)

@login_required
def account(request): # Used for updating user account

    if request.method == "POST":
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'{request.user.username}, you successfully updated your account!')
            return redirect('home')
    else:
        form = AccountUpdateForm(instance= request.user)

    context = {
        'form' : form,
    }
    return render(request, 'account/account.html', context)