from django.shortcuts import render
from django.http import HttpResponse
from .forms import HostForm, SkierForm
from django.views.generic.edit import FormView

def start(request):
    return render(request, 'main/start.html')

class HostFormView(FormView):
    template_name = 'host_form.html'
    form_class = HostForm
    success_url = '/done/'

    def form_valid(self, form):
        # TODO send email to coordinator
        return super().form_valid(form)

class SkierFormView(FormView):
    template_name = 'skier_form.html'
    form_class = SkierForm
    success_url = '/done/'

    def form_valid(self, form):
        # TODO send email to coordinator
        return super().form_valid(form)