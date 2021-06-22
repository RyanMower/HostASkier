from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from itertools import chain
from host.models import Host
from skier.models import Skier

def start(request):
    return render(request, 'main/start.html')

class MatchView(ListView):
    template_name = "match.html"
    context_object_name = "context"

    def get_queryset(self):
        queryset = {'hosts': Host.objects.all(), 
                    'skiers': Skier.objects.all()}
        return queryset
