from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreatingForm
# Create your views here.
class SignUpView(CreateView):
    '''
    Docstring for SignUpView
    '''
    form_class = CustomUserCreatingForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
