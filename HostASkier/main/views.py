from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def start(request):
    return render(request, 'main/start.html')


