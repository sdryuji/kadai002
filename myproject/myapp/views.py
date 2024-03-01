from django.shortcuts import render
from django.views.generic import TemplateView, ListView, SerchView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import Product
# from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

class TopView(TemplateView):
    template_name = "top.html"

class SerchView(LoginRequiredMixin, SerchView):
    template_name = "serch.html"


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'