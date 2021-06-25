from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from itertools import chain
from host.models import Host
from skier.models import Skier
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import HomeText
from .forms import StateForm


def home(request):
    data =  HomeText.objects.first()
    context = {}
    if data:
        context = {
            'data' : data,
        }
    else:
        context = {
            'data' : "No text was found for the home page."
        }
    return render(request, 'main/home.html', context)

class MatchView(AccessMixin,  ListView):
    template_name = "match.html"
    context_object_name = "context"

    def get_queryset(self):

        queryset = {
            'hosts' : Host.objects.all().filter(approved=True), 
            'skiers': Skier.objects.all().filter(approved=True),
            'form'  : StateForm(self.request.POST or None),
        }

        if self.request.method == "POST":
            if request.POST.get('state'):
                queryset = {
                    'hosts': Host.objects.all().filter(approved=True).filter(state=self.request.POST.get('state')), 
                    'skiers': Skier.objects.all().filter(approved=True).filter(state=self.request.POST.get('state')),
                }

        
        return queryset

    def dispatch(self, request, *args, **kwargs):
        authenticated = False
        if request.user.is_authenticated:
            authenticated = True
            if request.user.approved:
                return super().dispatch(request, *args, **kwargs)
                
        if authenticated:
            messages.error(request, f"{request.user.username}, your account is not approved!")
        else:
            messages.error(request, "Your are not signed in!")
        return redirect('home')
