from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# estoque\urls.py
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")