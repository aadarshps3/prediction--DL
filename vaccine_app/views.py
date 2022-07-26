from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from vaccine_app.forms import LoginRegister, UserRegister


def home(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_center:
                return redirect('center_home')
            elif user.is_nurse:
                return redirect('nurse_home')
            elif user.is_user:
                return redirect('user_home')
        else:
            messages.info(request, 'INVALID CREDENTIALS')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def user_register(request):
    login_form = LoginRegister()
    user_form = UserRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = UserRegister(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            u = user_form.save(commit=False)
            u.user = user
            u.save()
            messages.info(request, 'user Register successful')
            return redirect('login')
    return render(request, 'user_register.html', {'login_form': login_form, 'user_form': user_form})
