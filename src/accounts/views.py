from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from accounts.serializers import UserSerializer, GroupSerializer

# Create your views here.
from .models import *
from .forms import CreateUserForm

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

#homepage view
def home_view(request, *args, **kwargs): #args, keywordargs
	return render(request, "accounts/home_view.html", {})

def registerUserPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        #print("here")
        if form.is_valid():
            #print("valid")
            form.save()
                
    context = {'form':form}
    return render(request, 'accounts/user_register.html', context)
