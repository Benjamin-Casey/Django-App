from django.contrib import admin

# Register your models here.
from .models import User, Group, Alarm

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Alarm)
