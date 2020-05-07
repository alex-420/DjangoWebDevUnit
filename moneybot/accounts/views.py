from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class RegisterUser(CreateView):
    form_class = forms.RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'
