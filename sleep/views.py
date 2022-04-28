from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import User, Group

def index(request):
    users = User.objects.all()
    # output = ', '.join([u for u in users])
    return HttpResponse(users)

# --- #

def user_info(request, user_id):
    return HttpResponse("This is user id %s" % user_id)

def group_info(request, group_id):
    return HttpResponse("This is group id %s" % group_id)
