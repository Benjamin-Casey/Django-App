from django.db import models

# Many-to-many relationships
# https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_many/

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Alarm(models.Model):
    time = models.DateTimeField()
    repeat = models.CharField(max_length=32)


class Group(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)
    alarms = models.ManyToManyField(Alarm)

    def __str__(self):
        return self.name
