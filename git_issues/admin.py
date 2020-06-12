from django.contrib import admin
from git_issues.models import GithubIssues, GithubUsers, Labels
# Register your models here.
admin.site.register(GithubIssues)
admin.site.register(GithubUsers)
admin.site.register(Labels)
