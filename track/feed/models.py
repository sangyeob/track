from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class Channel(models.Model):
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField(max_length=500, blank=True)
	is_team_channel = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name

class Issue(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(max_length=1000)
	created_at = models.DateTimeField(default=datetime.now)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	PRIORITY_CHOICES = (
		(4, 'Critical'),
        (3, 'Major'),
        (2, 'Normal'),
        (1, 'Minor'),
        (0, 'General'),
	)
	priority = models.IntegerField(choices=PRIORITY_CHOICES)
	channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

class Task(models.Model):
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='tasks')
	job = models.TextField(max_length=200)
	assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Comment(models.Model):
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
	content = models.TextField(max_length=500)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	created_at = models.DateTimeField(default=datetime.now)

