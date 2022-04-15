from django.shortcuts import render


def userSite(request):
    return render(request, 'userSite.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'Register Page.html')


def package(request):
    return render(request, 'package.html')


def booking(request):
    return render(request, 'booking.html')


def usersitelog(request):
    return render(request, 'userSiteLog.html')