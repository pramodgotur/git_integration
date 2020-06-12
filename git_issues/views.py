from git_issues.api_helper.pagination import CustomPagination
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from git_issues.models import GithubIssues


def home(request):
    return render(request, 'home.html')


@api_view(['GET'])
def issues_view(request):
    context = {"status": True,
               "message": "successfully retrived issues", "data": []}
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
