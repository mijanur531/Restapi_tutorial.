from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.
def home(request):
    return HttpResponse("Hello, World!")
def about(request):
    return HttpResponse("About Page")
def contact(request):
    return HttpResponse("Contact Page")
