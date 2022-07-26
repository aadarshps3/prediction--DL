from django.contrib import messages
from django.shortcuts import render, redirect

from vaccine_app.forms import ScheduleForm
from vaccine_app.models import Vaccine, Center, Schedule


def nurse_home(request):
    return render(request, 'nurse_temp/nurse_home.html')


def center_view_n(request):
    c = Center.objects.all()
    context = {
        'center': c
    }
    return render(request, 'nurse_temp/center_view.html', context)


def vaccine_view_n(request):
    v = Vaccine.objects.all()
    context = {
        'vaccine': v
    }
    return render(request, 'nurse_temp/vaccine_view.html', context)


def schedule_add(request):
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_view')
    return render(request, 'nurse_temp/schedule_add.html', {'form': form})


def schedule_view(request):
    s = Schedule.objects.all()
    context = {
        'schedule': s
    }
    return render(request, 'nurse_temp/schedule_view.html', context)


def schedule_update(request, id):
    s = Schedule.objects.get(id=id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST or None, instance=s)
        if form.is_valid():
            form.save()
            messages.info(request, 'vaccine updated successful')
            return redirect('schedule_view')
    else:
        form = ScheduleForm(instance=s)
    return render(request, 'nurse_temp/schedule_update.html', {'form': form})


def schedule_delete(request, id):
    s = Schedule.objects.get(id=id)
    if request.method == 'POST':
        s.delete()
        return redirect('schedule_view')
    else:
        return redirect('schedule_view')
