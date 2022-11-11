from django.contrib import messages
from django.shortcuts import render, redirect

from vaccine_app.models import Vaccine, Center, Schedule, User, Appointment


def user_home(request):
    return render(request, 'user_temp/index.html')


def center_view_u(request):
    c = Center.objects.all()
    context = {
        'center': c
    }
    return render(request, 'user_temp/center_view.html', context)


def vaccine_view_u(request):
    v = Vaccine.objects.all()
    context = {
        'vaccine': v
    }
    return render(request, 'user_temp/vaccine_view.html', context)


def schedule_view_u(request):
    s = Schedule.objects.all()
    context = {
        'schedule': s
    }
    return render(request, 'user_temp/schedule_view.html', context)


def book_appointment(request, id):
    s = Schedule.objects.get(id=id)
    u = User.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u, schedule=s)
    if appointment.exists():
        messages.info(request, 'you have already requested appointment for this schedule')
        return redirect('schedule_view_u')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appointment Booked successful')
            return redirect('appointment_view')
    return render(request, 'user_temp/book_appointments.html', {'schedule': s})


def appointment_view(request):
    u = User.objects.get(user=request.user)
    a = Appointment.objects.filter(user=u)
    return render(request, 'user_temp/appointment_view.html', {'appointment': a})
