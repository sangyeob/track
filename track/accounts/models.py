from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
	name = models.CharField(max_length=100)

class Person(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=50)
	birth_date = models.DateField(null=True, blank=True)
	bio = models.TextField(max_length=500, blank=True)