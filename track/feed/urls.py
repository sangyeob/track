from django.urls import path

from . import views

app_name = 'feed'
urlpatterns = [
	path('', views.dashboardView, name='dashboardView'),
	path('channel/<str:channel_name>', views.channelView, name='channelView'),
	path('issue/<int:issue_id>/comment', views.issueCommentView, name="issueCommentView"),
	path('issue/<int:issue_id>/task', views.issueTaskView, name="issueTaskView"),
]