from django import forms
from django.contrib.auth.forms import UserCreationForm

from vaccine_app.models import Login, Center, Nurse, User, Vaccine, Schedule


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class CenterRegister(forms.ModelForm):
    class Meta:
        model = Center
        fields = ('name', 'place', 'address', 'contact_no')


class NurseRegister(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ('name', 'contact_no', 'email', 'address', 'center')


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class UserRegister(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = ('name', 'age', 'gender', 'contact_no', 'address')


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ('name', 'description')


class ScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Schedule
        fields = ('center', 'date', 'start_time', 'end_time')
