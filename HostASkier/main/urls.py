from django.urls import path
from . import views
from skier import views as skier_views
from host import views as host_views

urlpatterns = [
    path('', views.start, name='home'),
]