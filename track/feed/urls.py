from django.urls import path

from . import views

app_name = 'feed'
urlpatterns = [
	path('', views.myPageView, name='myPageView'),
	path('channel/<str:channel_name>', views.channelView, name='channelView'),
	path('user/<str:user_name>', views.userView, name="userView"),
	path('issue', views.newIssueView, name='newIssueView'),
	path('issue/<int:issue_id>', views.issueView, name="issueView"),
	path('issue/<int:issue_id>/comment', views.issueCommentView, name="issueCommentView"),
]