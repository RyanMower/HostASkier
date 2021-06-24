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


def start(request):
    return render(request, 'main/start.html')

class MatchView( AccessMixin,  ListView):
    template_name = "match.html"
    context_object_name = "context"

    def get_queryset(self):
        queryset = {'hosts': Host.objects.all().filter(approved=True), 
                    'skiers': Skier.objects.all().filter(approved=True)}
        return queryset

    def dispatch(self, request, *args, **kwargs):
        authenticated = False
        if request.user.is_authenticated:
            authenticated = True
            if request.user.approved:
                return self.super.dispatch()
                
        if authenticated:
            messages.error(request, "Your account is not approved!")
        else:
            messages.error(request, "Your are not signed in!")
        return redirect('home')
