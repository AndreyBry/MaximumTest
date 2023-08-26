from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .forms import UserRegisterForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect_url = reverse('login')
            return redirect(redirect_url)
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'app_auth/register.html', context)


def login_view(request):
    redirect_url = reverse('profile')

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        return render(request, 'app_auth/login.html')

    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(redirect_url)
        return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден'})


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')


@login_required(login_url=reverse_lazy('login'))
def logout_view(request):
    logout(request)
    redirect_url = reverse('login')
    return redirect(redirect_url)
