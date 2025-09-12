
from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Hello World Tina in the browser")