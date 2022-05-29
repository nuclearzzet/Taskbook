from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return HttpResponse("<h1>About Us</h1>")