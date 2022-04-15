# Create your views here.
from django.http import HttpResponse
from .models import Booking
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return HttpResponse("Welcome")


def booking_by_id(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return HttpResponse(
        f"Pet Name: {booking.pet_name}, Owner Name: {booking.owner_name}, Owner Phone Number: {booking.owner_phone_number}, Grooming Package: {booking.grooming_package}, Grooming Session: {booking.grooming_session}")


# user site


def home(request):
    return render(request, 'home.html')


def register(request):
    form = UserCreationForm
    return render(request, 'registration/register.html', {'form': form})
