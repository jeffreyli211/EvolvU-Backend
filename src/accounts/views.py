from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *

#homepage view
def home_view(request, *args, **kwargs): #args, keywordargs
	return render(request, "accounts/home_view.html", {})

def registerUserPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("here")
        if form.is_valid():
            print("valid")
            form.save()
                
    context = {'form':form}
    return render(request, 'accounts/user_register.html', context)
