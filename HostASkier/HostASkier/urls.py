"""hostaskier_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account import views as account_views
from main import views as main_views
from skier import views as skier_views
from host import views as host_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', account_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
    path('pending-skiers', skier_views.pending_skiers_view, name='pendingskiers'),
    path('pending-hosts', host_views.pending_hosts_view, name='pendinghosts'),
    path('pending-coordinators', account_views.pending_coordinators_view, name='pendingcoordinators'),
    path('become-a-skier', skier_views.SkierFormView.as_view(template_name='skier/skier_form.html'), name='becomeaskier'),
    path('become-a-host', host_views.HostFormView.as_view(template_name='host/host_form.html'), name='becomeahost'),
    path('match/', main_views.match_view, name='match'),
    #path('match/', main_views.MatchView.as_view(template_name='main/match.html'), name='match'),
    path('account/', account_views.account, name='account'),
    path('host/<int:pk>/', host_views.HostDetailView.as_view(), name="host-detail"),
    path('skier/<int:pk>/', skier_views.SkierDetailView.as_view(), name="skier-detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
