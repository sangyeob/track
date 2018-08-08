from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

import json

from .models import *
from accounts.models import *

@login_required
def dashboardView(request):
	return render(request, 'feed/channel.html', context={
		'channel_name': 'dashboard',	
		'channels': Channel.objects.filter(is_team_channel=False),
		'is_dashboard': True,
	})

@login_required
def channelView(request, channel_name):
	channel = get_object_or_404(Channel, name=channel_name)
	if channel.is_team_channel:
		team = Team.objects.get(team_channel=channel)
		members = User.objects.filter(person__team=team)	
	else:
		members = User.objects.all()
	
	return render(request, 'feed/channel.html', context={
		'channel_name': channel_name,
		'channels': Channel.objects.filter(is_team_channel=False),
		'issues': Issue.objects.select_related().all().filter(channel = channel),
		'members': members,
	})

@login_required
def issueCommentView(request, issue_id):
	if request.method == 'POST':
		try:
			author = request.POST['author']
			content = request.POST['content']
			c = Comment(issue=Issue.objects.get(pk=issue_id), 
					 author=User.objects.get(pk=author), 
					 content=content)
			c.save()
			return JsonResponse({
				'message': 'success',
				'content': c.content,
				'team_name': c.author.person.team.name,
				'author': c.author.person.name,
				'pic': c.author.person.profile_image_url,
				})
		except:
			return JsonResponse({
				'message': 'failed',
				})
	return HttpResponse("post only")

@login_required
def issueTaskView(request, issue_id):
	if request.method == 'POST':
		try:
			assigned_to = request.POST['assigned_to']
			job = request.POST['job']
			t = Task(issue=Issue.objects.get(pk=issue_id), 
					 assigned_to=User.objects.get(pk=assigned_to), 
					 job=job)
			t.save()
			return HttpResponse("success")
		except:
			return HttpResponse("failed")
	return HttpResponse("post only")