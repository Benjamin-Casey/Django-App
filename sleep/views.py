from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, BeddyByeBoys! You\'re at the sleep index!')
    
