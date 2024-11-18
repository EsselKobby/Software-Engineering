from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationView
    success_url = reverse_lazy('login')
    template_name = 'signup.html'