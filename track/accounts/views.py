from django.shortcuts import render

def login(request):
	if request.method == 'POST':
		pass
	if request.method == 'GET':
		return render(request, 'accounts/login.html', context={ 
			'toast': {
				'message': 'hi',
				'type': 'general'
			},
		})