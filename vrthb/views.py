from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def index(request):
    array = ['ubuntu', 'active']
    return render(request, "base.html", context={'list': array, 'is_homepage': True})


def create_view(request):
    if request.method == 'POST':
        return redirect('index_url')

    return render(request, 'vrthb/create.html')


@login_required()
def profile_view(request):
    return render(request, 'vrthb/profile_user.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            user = authenticate(username=user.username, password=password)
            if user:
                login(request, user)
                return redirect('profile_url')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
