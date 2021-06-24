from django.shortcuts import render
from django.http import HttpResponse
from .forms import SkierForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from skier.models import Skier
from django.urls import reverse_lazy


# Create your views here.
class SkierFormView(FormView):
    template_name = 'skier_form.html'
    form_class = SkierForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'Thank you! Your submission has been recorded.')
        return super().form_valid(form)

## Creates a skier
def become_a_skier_view(request):
    form = SkierForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, f'Thank you! Your submission has been recorded.')
        return render('home')
    else:
        messages.error(request, f'Please enter a valid address.')

    context = {
        'form' : form
    }
    return render(request, "skier/skier_form.html", context)

@login_required
def pending_skiers_view(request):
    ## Skiers approved by coordinator?
    if not request.user.approved:
        context = {
            'data' : []
        }
        return render(request, "main/not_approved_coordinator.html", context)
    
    if request.method == "POST":
        skier = Skier.objects.filter(id=request.POST['id']).first()
        if request.POST.get('status'):
            if request.POST.get('status') == "Accept":
                skier.approved = True
                skier.save()
            elif request.POST.get('status') == "Decline":
                skier.delete() ## Deletes the object from the database

    pending_skiers = Skier.objects.filter(approved=False)

    ## Check if there are any pending-coordinators to render
    if len(pending_skiers) == 0:
        context = None
        return render(request, "skier/no_pending_skiers.html", context)
    else:
        context = {
            'pending_skiers' : pending_skiers,
        }
        return render(request, "skier/pending_skiers.html", context)

