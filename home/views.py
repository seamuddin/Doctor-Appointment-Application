from django.shortcuts import render

# Create your views here.

def index(request, **kwargs):

    return render(request, 'index.html')


def login(request, **kwargs):

    return render(request, 'index.html')