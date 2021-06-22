from django.urls import path
from . import views
from skier import views as skier_views
from host import views as host_views

urlpatterns = [
    path('', views.start, name='home'),
    #path('host-form/', host_views.HostFormView.as_view(template_name='main/host_form.html'), name='hostform'),
    #path('skier-form/', skier_views.SkierFormView.as_view(template_name='main/skier_form.html'), name='skierform'),
]