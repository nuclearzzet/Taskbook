from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def signup(request):
    return HttpResponse("<h1>Register</h1>")