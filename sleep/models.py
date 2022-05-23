from django.db import models
from django.contrib.auth.models import Group

# Many-to-many relationships
# https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_many/

# Create your models here.

class Alarm(models.Model):
    name = models.CharField(max_length=128, default="Bed Time")
    time = models.DateTimeField()
    repeat = models.CharField(max_length=32)

    def __str__(self):
        return self.name


Group.add_to_class('alarms', models.ManyToManyField(Alarm, blank=True))
