from django.shortcuts import render

# Create your views here.

def index(request, **kwargs):
    if request.user:
        if hasattr(request.user, 'user_type'):
            if request.user.user_type == '1':
                return render(request, 'patient.html')

    return render(request, 'index.html')


def login(request, **kwargs):

    return render(request, 'index.html')