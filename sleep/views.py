from django.shortcuts import render
from django.template import loader

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Alarm

# Create your views here.
from django.http import HttpResponse
# from .models import User, Group

def index(request):
    # users = 'lol'
    template = loader.get_template('sleep/index.html')
    context = {
        # 'users': users, 
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("This is user id %s" % 'user_id')

# --- #

def user_info(request, user_id):
    return HttpResponse("This is user id %s" % user_id)

@login_required
def group_info(request, group_name):
    template = loader.get_template('sleep/group.html')
    group_data = Group.objects.get(name=group_name)
    context = {
        'group_data': group_data,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("This is group id %s" % group_name)

@login_required
def alarm_info(request, alarm_id):
    template = loader.get_template('sleep/alarm.html')
    alarm_data = Alarm.objects.get(id=alarm_id)
    context = {
        'alarm_data': alarm_data,
    }
    return HttpResponse(template.render(context, request))


# How to add/remove users to groups.

# myuser.groups.set([group_list])
# myuser.groups.add(group, group, ...)
# myuser.groups.remove(group, group, ...)
# myuser.groups.clear()
# myuser.user_permissions.set([permission_list])
# myuser.user_permissions.add(permission, permission, ...)
# myuser.user_permissions.remove(permission, permission, ...)
# myuser.user_permissions.clear()
