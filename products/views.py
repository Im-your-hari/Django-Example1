from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Index Page</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def contact(request):
    return HttpResponse('<h1>Contact Page</h1>')