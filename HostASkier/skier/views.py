from django.shortcuts import render
from django.http import HttpResponse
from .forms import SkierForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
class SkierFormView(FormView):
    template_name = 'skier_form.html'
    form_class = SkierForm
    success_url = '/done/'

    def form_valid(self, form):
        # TODO send email to coordinator
        return super().form_valid(form)

def become_a_skier_view(request):
    form = SkierForm(request.POST or None)

    if form.is_valid():
        form.save()
    else:
        messages.error(request, f'{request.user.username}\'s Please enter a valid address.')
    context = {
        'form' : form
    }
    return render(request, "main/skier_form.html", context)