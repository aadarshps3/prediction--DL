from django.contrib import messages
from django.shortcuts import render, redirect

from vaccine_app.forms import LoginRegister, CenterRegister, VaccineForm
from vaccine_app.models import Center, Login, Nurse, User, Vaccine


def admin_home(request):
    return render(request, 'admin_temp/admin_home.html')


def center_register(request):
    login_form = LoginRegister()
    center_form = CenterRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        center_form = CenterRegister(request.POST)
        if login_form.is_valid() and center_form.is_valid():
            user = login_form.save(commit=False)
            user.is_center = True
            user.save()
            c = center_form.save(commit=False)
            c.user = user
            c.save()
            messages.info(request, 'center Register successful')
            return redirect('center_view')
    return render(request, 'admin_temp/center_register.html', {'login_form': login_form, 'center_form': center_form})


def center_view(request):
    c = Center.objects.all()
    context = {
        'center': c
    }
    return render(request, 'admin_temp/center_view.html', context)


def center_update(request, id):
    c = Center.objects.get(id=id)
    l = Login.objects.get(center=c)
    if request.method == 'POST':
        form = CenterRegister(request.POST or None, instance=c)
        login_form = LoginRegister(request.POST or None, instance=l)
        if form.is_valid() and login_form.is_valid():
            form.save()
            login_form.save()
            messages.info(request, 'center updated successful')
            return redirect('center_view')
    else:
        form = CenterRegister(instance=c)
        login_form = LoginRegister(instance=l)
    return render(request, 'admin_temp/center_update.html', {'form': form, 'login_form': login_form})


def center_delete(request, id):
    e = Center.objects.get(id=id)
    c = Login.objects.get(center=e)
    if request.method == 'POST':
        c.delete()
        return redirect('center_view')
    else:
        return redirect('center_view')


def nurse_view(request):
    n = Nurse.objects.all()
    context = {
        'nurse': n
    }
    return render(request, 'admin_temp/nurse_view.html', context)


def user_view(request):
    u = User.objects.all()
    context = {
        'user': u
    }
    return render(request, 'admin_temp/user_view.html', context)


def user_delete(request, id):
    e = User.objects.get(id=id)
    u = Login.objects.get(user=e)
    if request.method == 'POST':
        u.delete()
        return redirect('user_view')
    else:
        return redirect('user_view')


def vaccine_add(request):
    form = VaccineForm()
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaccine_view')
    return render(request, 'admin_temp/vaccine_add.html', {'form': form})


def vaccine_view(request):
    v = Vaccine.objects.all()
    context = {
        'vaccine': v
    }
    return render(request, 'admin_temp/vaccine_view.html', context)


def vaccine_update(request, id):
    v = Vaccine.objects.get(id=id)
    if request.method == 'POST':
        form = VaccineForm(request.POST or None, instance=v)
        if form.is_valid():
            form.save()
            messages.info(request, 'vaccine updated successful')
            return redirect('vaccine_view')
    else:
        form = VaccineForm(instance=v)
    return render(request, 'admin_temp/vaccine_update.html', {'form': form})


def vaccine_delete(request, id):
    v = Vaccine.objects.get(id=id)
    if request.method == 'POST':
        v.delete()
        return redirect('vaccine_view')
    else:
        return redirect('vaccine_view')
