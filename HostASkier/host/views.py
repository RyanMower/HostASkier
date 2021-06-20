from django.shortcuts import render
from django.http import HttpResponse
from .forms import HostForm
from skier.forms import SkierForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from host.models import Host


class HostFormView(FormView):
    template_name = 'host_form.html'
    form_class = HostForm
    success_url = '/done/'

    def form_valid(self, form):
        # TODO send email to coordinator
        return super().form_valid(form)

def become_a_host_view(request):
    form = HostForm(request.POST or None)

    if form.is_valid():
        print("Saving")
        form.save()
    else:
        messages.error(request, f'{request.user.username}\'s Please enter a valid address.')
    context = {
        'form' : form
    }
    return render(request, "host/host_form.html", context)

@login_required
def pending_hosts_view(request):
    if request.user.approved:
        form = HostForm(request.POST or None)

        if form.is_valid():
            form.save()
        else:
            messages.error(request, f'{request.user.username}\'s Please enter a valid address.')
        context = {
            'pending_hosts' : Host.objects.filter(approved=False)
        }
        ## Check if NONE, then render different page
        return render(request, "host/pending_host_form.html", context)
    else: ## Not approved by admin
        context = {
            'data' : []
        }
        return render(request, "main/not_approved_coordinator.html", context)