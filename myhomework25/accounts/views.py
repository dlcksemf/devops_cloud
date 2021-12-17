from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/signup.html",
)

login = LoginView.as_view()

profile = TemplateView.as_view()

logout = LogoutView.as_view()