from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import Person

def loginView(request):
	if request.method == 'POST':
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			try:
				person = Person.objects.get(user=user)
			except:
				person = Person(user=user)
				person.save()
				
			if person.name == '' or person.team == None:
				return HttpResponseRedirect(reverse('accounts:updatePersonProfileView'))
			return HttpResponseRedirect(reverse('feed:myPageView'))
		else:
			return render(request, 'accounts/login.html', context={ 
				'toast': {
					'message': 'Login Failed',
					'type': 'error'
				},
			})

	if request.method == 'GET':
		if request.user:
			if request.user.is_authenticated:
				person = Person.objects.get(user=request.user)
				if person.name == '' or person.team == None:
					return HttpResponseRedirect(reverse('accounts:updatePersonProfileView'))
				return HttpResponseRedirect(reverse('feed:myPageView'))
			else: 
				logout(request)
		return render(request, 'accounts/login.html', context={})

def logoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse('accounts:loginView'))

def updatePersonProfileView(request):
	return render(request, 'accounts/updatePersonProfile.html')