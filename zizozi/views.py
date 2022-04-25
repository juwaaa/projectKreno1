from django.shortcuts import render, redirect

from zizozi.forms import NewUserForm
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def userSite(request):
    return render(request, 'userSite.html')


def login(request):
    return render(request, 'login.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # message = 'Save complete'
            messages.success(request, "Registration successful.")
            return redirect("/admin")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def package(request):
    return render(request, 'package.html')


def booking(request):
    return render(request, 'booking.html')


def usersitelog(request):
    return render(request, 'userSiteLog.html')
