from django.contrib import admin
from django.urls import path
from git_issues.views import issues_view, labels_view, assinees_view

urlpatterns = [
    path("api/issues/", issues_view),
    path("api/labels/", labels_view),
    path("api/assignees/", assinees_view),
]
