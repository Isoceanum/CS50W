
from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    return render(request, "hei/index.html")


def petter(request):
    return HttpResponse("Hello, petter!")


def hils(request, name):
    return render(request, "hei/hilsen.html", {
        "name": name.capitalize()
    })
