from django.shortcuts import render


def login(request, **kwargs):
    return render(request, 'login.html')
