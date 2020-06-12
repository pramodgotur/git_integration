from django.contrib import admin
from django.urls import path
from git_issues.views import issues_view

urlpatterns = [
    path("api/issues/", issues_view),
]
