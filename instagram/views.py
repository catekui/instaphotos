from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm
from .models import *

# Create your views here.
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request,'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('login')

    context = {'form': form}
    return render(request,'register.html', context)

def index(request):
    return render(request,'index.html')

