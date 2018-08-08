from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse

import json

from .models import *
from accounts.models import *

@login_required
def myPageView(request):
	return render(request, 'feed/channel.html', context={
		'channel_name': 'myPage',	
		'channels': Channel.objects.filter(is_team_channel=False),
		'issues': Issue.objects.filter(author=request.user).order_by('-priority', '-created_at'),
		'is_myPage': True,
	})

@login_required
def channelView(request, channel_name):
	channel = get_object_or_404(Channel, name=channel_name)
	
	return render(request, 'feed/channel.html', context={
		'channel_name': channel_name,
		'channel_desc': channel.description,
		'channels': Channel.objects.filter(is_team_channel=False),
		'issues': Issue.objects.select_related().all().filter(channel = channel).order_by('-priority', '-created_at'),
	})

@login_required
def userView(request, user_name):
	user = User.objects.get(username=user_name)
	req_person = Person.objects.get(user=request.user)

	if user.person == req_person:
		return HttpResponseRedirect(reverse('feed:myPageView'))

	if req_person.team == user.person.team:
		issues = Issue.objects.select_related().all().filter(author__username=user_name)
	else:	
		issues = Issue.objects.select_related().all().filter(author__username=user_name, channel__is_team_channel=False)

	return render(request, 'feed/channel.html', context={
		'page_user': user,
		'channels': Channel.objects.filter(is_team_channel=False),
		'issues': issues.order_by('-priority', '-created_at'),
		'is_myPage': True,
		'needPageDescription': True,
	})

@login_required
def newIssueView(request):
	channel = get_object_or_404(Channel, name=request.POST['channel_name'])
	print(request.POST)
	issue = Issue(author=request.user,
				  title=request.POST['title'],
				  priority=request.POST['priority'],
				  content=request.POST['content'],
				  channel=channel)
	issue.save()
	'''if request.method == 'POST':
					try:
						channel = get_object_or_404(Channel, name=request.POST['channel_name'])
						issue = Issue(author=request.user,
									  title=request.POST['title'],
									  priority=request.POST['priority'],
									  content=request.POST['content'],
									  channel=channel)
						issue.save()
					except:
						pass'''
	return HttpResponseRedirect(reverse('feed:channelView', kwargs={'channel_name': request.POST['channel_name']}))


@login_required
def issueView(request, issue_id):
	if request.method == 'DELETE':
		try:
			issue = Issue.objects.get(pk=issue_id)
			if issue.author != request.user:
				return JsonResponse({
					'message': 'failed'
				})	
			issue.delete()
			return JsonResponse({
				'message': 'success'
			})
		except:
			return JsonResponse({
				'message': 'failed'
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