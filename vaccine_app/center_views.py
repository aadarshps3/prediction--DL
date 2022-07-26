from django.contrib import messages
from django.shortcuts import render, redirect

from vaccine_app.forms import LoginRegister, NurseRegister
from vaccine_app.models import Nurse, Login, Vaccine, Appointment


def center_home(request):
    return render(request, 'center_temp/center_home.html')


def nurse_register(request):
    login_form = LoginRegister()
    nurse_form = NurseRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        nurse_form = NurseRegister(request.POST)
        if login_form.is_valid() and nurse_form.is_valid():
            user = login_form.save(commit=False)
            user.is_nurse = True
            user.save()
            n = nurse_form.save(commit=False)
            n.user = user
            n.save()
            messages.info(request, 'Nurse Register successful')
            return redirect('nurse_view')
    return render(request, 'center_temp/nurse_register.html', {'login_form': login_form, 'nurse_form': nurse_form})


def nurse_view(request):
    n = Nurse.objects.all()
    context = {
        'nurse': n
    }
    return render(request, 'center_temp/nurse_view.html', context)


def nurse_update(request, id):
    n = Nurse.objects.get(id=id)
    l = Login.objects.get(nurse=n)
    if request.method == 'POST':
        form = NurseRegister(request.POST or None, instance=n)
        login_form = LoginRegister(request.POST or None, instance=l)
        if form.is_valid() and login_form.is_valid():
            form.save()
            login_form.save()
            messages.info(request, 'center updated successful')
            return redirect('nurse_view')
    else:
        form = NurseRegister(instance=n)
        login_form = LoginRegister(instance=l)
    return render(request, 'center_temp/nurse_update.html', {'form': form, 'login_form': login_form})


def nurse_delete(request, id):
    e = Nurse.objects.get(id=id)
    n = Login.objects.get(nurse=e)
    if request.method == 'POST':
        n.delete()
        return redirect('nurse_view')
    else:
        return redirect('nurse_view')


def vaccine_view_c(request):
    v = Vaccine.objects.all()
    context = {
        'vaccine': v
    }
    return render(request, 'center_temp/vaccine_view.html', context)


def appointment_center(request,id):
    a = Appointment.objects.get(id=id)
    context = {
        'appointment': a
    }
    return render(request, 'center_temp/appointment_view.html', context)
