from git_issues.api_helper.pagination import CustomPagination
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from git_issues.models import GithubIssues, Labels, GithubUsers
import arrow
from django.utils import timezone
from datetime import timedelta


def home(request):
    """
        All issues are listed in this view
    """
    return render(request, 'home.html')


@api_view(['GET'])
def issues_view(request):
    """
        This api view return all repo issues
    """
    context = {"status": True,
               "message": "successfully retrived issues", "data": []}
    filter_label = request.GET.get('label', None)
    filter_assignee = request.GET.get('assignee', None)
    no_of_days = request.GET.get('no_of_days', None)
    if no_of_days:
        filter_datetime = timezone.now()-timedelta(days=int(no_of_days))
        issues = GithubIssues.objects.filter(
            issue_created_at__gte=filter_datetime)
    else:
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
        fmt = "DD MMM YYYY, HH:mm ZZ"
        issue_detail['issue_created_at'] = arrow.get(
            issue.issue_created_at).to("Asia/Kolkata").format(fmt)
        issue_detail['issue_url'] = issue.issue_url
        issue_detail['state'] = issue.state
        context['data'].append(issue_detail)
    result_page = paginator.paginate_queryset(context['data'], request)
    data = paginator.get_paginated_response(result_page)
    return Response(data=data.data, status=HTTP_200_OK)


@api_view(['GET'])
def labels_view(request):
    """
        This api view return labels
    """
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
    """
        This api view return assinees
    """
    context = {"status": True,
               "message": "successfully retrived assignees", "data": []}
    assignees = GithubUsers.objects.all()
    for assignee in assignees:
        assignee_detail = {}
        assignee_detail['id'] = assignee.id
        assignee_detail['login_name'] = assignee.login_name
        context['data'].append(assignee_detail)
    return Response(data=context, status=HTTP_200_OK)
