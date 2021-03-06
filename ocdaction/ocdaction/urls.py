"""ocdaction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from core.views import HomepageView, ContactView, AboutView, ActView, MeetTheTeam, TermsAndConditions, ThinkView
from profiles.views import LoginView, RegistrationView, RegistrationComplete, ActivationComplete
from profiles.forms import OCDActionUserRegistrationForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomepageView.as_view(), name="index"),
    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^contact', ContactView.as_view(), name="contact"),
    url(r'^about', AboutView.as_view(), name="about"),
	url(r'^act', ActView.as_view(), name="act"),
    url(r'^meet-the-team', MeetTheTeam.as_view(), name="team"),
    url(r'^think', ThinkView.as_view(), name="think"),
    url(r'^terms-and-conditions', TermsAndConditions.as_view(), name="terms_and_conditions"),
    url(r'^accounts/register', RegistrationView.as_view(form_class=OCDActionUserRegistrationForm), name='registration_register'),
    url(r'^accounts/registration-complete/', RegistrationComplete.as_view(), name='registration_complete'),
    url(r'^accounts/activate/complete/', ActivationComplete.as_view(), name='activation_complete'),
    url(r'^accounts/', include('registration.backends.default.urls')),

]
