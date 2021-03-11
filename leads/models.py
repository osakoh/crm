from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Agent(models.Model):  # one agent to many leads
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Lead(models.Model):  # many leads assigned to an Agent
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)


"""agent = models.ForeignKey("Agent") # using double quotes around the class allows the parent class to be referenced 
if it's below its child class 
"""
