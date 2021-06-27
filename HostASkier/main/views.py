from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin
from django.views.generic.edit import FormMixin
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
    print(type(data))
    context = {}
    if data:
        context = {
            'data' : data.Home_Text,
        }
    else:
        context = {
            'data' : "No text was found for the home page."
        }
    return render(request, 'main/home.html', context)

class MatchView(AccessMixin, ListView):
    template_name = "match.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super(MatchView, self).get_context_data(**kwargs)
        context["form"] = StateForm()
        return context

    def get_queryset(self):
        queryset = {
                    'hosts' : Host.objects.all().filter(approved=True), 
                    'skiers': Skier.objects.all().filter(approved=True),
            }
        if self.request.method == 'POST':
            form = StateForm(request.POST)
            if form.cleaned_data.get['filter_on_state']:
                fstate = form.cleaned_data['state']
                queryset = {
                        'hosts' : Host.objects.all().filter(approved=True).filter(state=fstate),
                        'skier' : Skier.objects.all().filter(approved=True).filter(state=fstate),
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

@login_required
def match_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "You are not signed in")
        return redirect('/')
    if not request.user.approved:
        messages.error(request, f"{request.user.username}, your account is not approved!")
        return redirect('/')
   
    if request.method == "POST":
        form = StateForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['enable_filter']:
                fstate = form.cleaned_data['state']
                print(f"Filtering on {fstate}")
                queryset = {
                        'hosts' : Host.objects.all().filter(approved=True).filter(state=fstate),
                        'skiers' : Skier.objects.all().filter(approved=True).filter(state=fstate),
                    }
            else: ## Don't want to filter on state
                queryset = {
                    'hosts' : Host.objects.all().filter(approved=True),
                    'skiers': Skier.objects.all().filter(approved=True),
                }
        else: ## Form is not valid
            queryset = {
                    'hosts' : None,
                    'skiers' : None,
                }

    else: ## Method is GET
        queryset = {
                'hosts' : Host.objects.all().filter(approved=True),
                'skiers': Skier.objects.all().filter(approved=True),
            }

    context = {
            'hosts' : queryset['hosts'],
            'skiers' : queryset['skiers'],
            'form' : StateForm(),
        }
    
    return render(request, "main/match.html", context)
