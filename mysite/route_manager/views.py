from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    return render(request, 'index.html')

def index(request):
    print(request)
    return HttpResponse("<h1>Hello, world. You're at the main page.</h1> hello")
