from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def current_projects(request):
    return render(request, 'current_projects.html')


def past_projects(request):
    return render(request, 'past_projects.html')
