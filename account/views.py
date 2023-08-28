from django.shortcuts import render

#importing createview
from django.views.generic.edit import CreateView

#importing userCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    #if the signup is successful then the destination we want to go, we have to write that destination in the "reverse_lazy". 
    #Here we write login because we want to go to login after a successful signup.
    success_url = reverse_lazy('login')

    template_name = 'registration/sign_up.html'