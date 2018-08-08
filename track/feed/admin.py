from django.contrib import admin
from .models import Channel, Issue, Comment

class ChannelAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'is_team_channel']

admin.site.register(Channel, ChannelAdmin)

class IssueAdmin(admin.ModelAdmin):
	fields = ['title', 'content', 'created_at', 'author', 'priority', 'channel']

admin.site.register(Issue, IssueAdmin)

class CommentAdmin(admin.ModelAdmin):
	fields = ['issue', 'content', 'author', 'created_at']

admin.site.register(Comment, CommentAdmin)

