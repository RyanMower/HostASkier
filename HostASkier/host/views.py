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
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def become_a_host_view(request):
    form = HostForm(request.POST or None)

    if form.is_valid():
        print("Saving")
        form.save()
        return render(request, "host/host_form.html", context)
    else:
        messages.error(request, f'{request.user.username}\'s Please enter a valid address.')
    context = {
        'form' : form
    }
    return render(request, "host/host_form.html", context)

@login_required
def pending_hosts_view(request):
    ## Coordinator approved by coordinator?
    if not request.user.approved:
        context = {
            'data' : []
        }
        return render(request, "main/not_approved_coordinator.html", context)
    
    if request.method == "POST":
        host = Host.objects.filter(id=request.POST['id']).first()
        if request.POST.get('status'):
            if request.POST.get('status') == "Accept":
                host.approved = True
                host.save()
            elif request.POST.get('status') == "Decline":
                host.delete() ## Deletes the object from the database

    pending_hosts = Host.objects.filter(approved=False)

    ## Check if there are any pending-coordinators to render
    if len(pending_hosts) == 0:
        context = None
        return render(request, "host/no_pending_hosts.html", context)
    else:
        context = {
            'pending_hosts' : pending_hosts,
        }
        return render(request, "host/pending_hosts.html", context)

