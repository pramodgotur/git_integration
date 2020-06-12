from git_issues.api_helper.pagination import CustomPagination
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from git_issues.models import GithubIssues, Labels, GithubUsers


def home(request):
    return render(request, 'home.html')


@api_view(['GET'])
def issues_view(request):
    context = {"status": True,
               "message": "successfully retrived issues", "data": []}
    filter_label = request.GET.get('label', None)
    filter_assignee = request.GET.get('assignee', None)
    if filter_label and filter_assignee:
        issues = GithubIssues.objects.filter(
            labels__id__in=[filter_label], assignees__id__in=[filter_assignee])
    elif filter_label:
        issues = GithubIssues.objects.filter(labels__id__in=[filter_label])
    elif filter_assignee:
        issues = GithubIssues.objects.filter(
            assignees__id__in=[filter_assignee])
    else:
        issues = GithubIssues.objects.all()
    paginator = CustomPagination()
    for issue in issues:
        issue_detail = {}
        issue_detail['id'] = issue.id
        issue_detail['title'] = issue.title
        issue_detail['issue_number'] = issue.issue_number
        issue_detail['issue_created_at'] = issue.issue_created_at
        issue_detail['issue_url'] = issue.issue_url
        issue_detail['state'] = issue.state
        context['data'].append(issue_detail)
    result_page = paginator.paginate_queryset(context['data'], request)
    data = paginator.get_paginated_response(result_page)
    return Response(data=data.data, status=HTTP_200_OK)


@api_view(['GET'])
def labels_view(request):
    context = {"status": True,
               "message": "successfully retrived labels", "data": []}
    labels = Labels.objects.all()
    for label in labels:
        label_detail = {}
        label_detail['id'] = label.id
        label_detail['name'] = label.name
        context['data'].append(label_detail)
    return Response(data=context, status=HTTP_200_OK)


@api_view(['GET'])
def assinees_view(request):
    context = {"status": True,
               "message": "successfully retrived assignees", "data": []}
    assignees = GithubUsers.objects.all()
    for assignee in assignees:
        assignee_detail = {}
        assignee_detail['id'] = assignee.id
        assignee_detail['login_name'] = assignee.login_name
        context['data'].append(assignee_detail)
    return Response(data=context, status=HTTP_200_OK)
