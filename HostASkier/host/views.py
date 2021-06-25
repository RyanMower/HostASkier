from django.shortcuts import render
from django.http import HttpResponse
from .forms import HostForm
from skier.forms import SkierForm
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from host.models import Host
from django.shortcuts import redirect
from django.urls import reverse_lazy

class HostFormView(FormView):
    template_name = 'host_form.html'
    form_class = HostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'Thank you {form.cleaned_data.get("name")}! Your submission has been recorded.')
        return super().form_valid(form)

class HostDetailView(DetailView):
    model = Host

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

def become_a_host_view(request):
    form = HostForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, f'Thank you! Your submission has been recorded.')
        return render('home')

    else:
        messages.error(request, f'Please enter a valid address.')

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

