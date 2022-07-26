from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_center = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class Center(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='center')
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    address = models.TextField(max_length=50)
    contact_no = models.CharField(max_length=50)

    def __str__(self):
        return self.na+me


class Nurse(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='nurse')
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField(max_length=50)
    center = models.ForeignKey(Center, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    address = models.TextField()
    recent_vaccinations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    vaccine_name = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING,null=True,blank=True)
    vaccinated = models.BooleanField(default=False)
