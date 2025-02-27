from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def character2(request):
    return render(request, "mydei.html")
