from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, BeddyByeBoys! You\'re at the Payment System!')
    
def user_info(request, user_id):
    return HttpResponse("This is user %s." % user_id)

def group_info(request, group_id):
    return HttpResponse("This is group %s." % group_id)