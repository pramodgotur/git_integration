from git_issues.models import GithubIssues, GithubUsers, Labels
from git_issues.api_helper.git_issues_api import get_issues, get_repo

repo = get_repo()


def sync_assignees(repo):
    assignees = repo.get_assignees()
    bulk_assignee_objs = []
    existing_users = GithubUsers.objects.values_list('login_name')
    print(existing_users)
    for assignee in assignees:
        assignee_login = assignee.login
        if (assignee_login,) not in existing_users:
            assignee_obj = GithubUsers()
            assignee_obj.login_name = assignee.login
            bulk_assignee_objs.append(assignee_obj)
    if bulk_assignee_objs:
        GithubUsers.objects.bulk_create(bulk_assignee_objs)


def sync_labels(repo):
    labels = repo.get_labels()
    bulk_label_objs = []
    existing_labels = Labels.objects.values_list('name')
    print(existing_labels)
    for label in labels:
        label_name = label.name
        if (label_name,) not in existing_labels:
            label_obj = Labels()
            label_obj.name = label_name
            bulk_label_objs.append(label_obj)
    if bulk_label_objs:
        Labels.objects.bulk_create(bulk_label_objs)


def sync_issues():
    global repo
    sync_assignees(repo)
    sync_labels(repo)
    # issues = get_issues(repo, state="all")
    issues = get_issues(repo)
    bulk_issue_objects = []
    all_issue_assignees = []
    existing_issues = GithubIssues.objects.values_list('issue_number')
    print(existing_issues)
    for issue in issues:
        if issue.pull_request is None:
            issue_number = issue.number
            if (issue_number,) not in existing_issues:
                issue_obj = GithubIssues()
                issue_obj.title = issue.title
                issue_obj.issue_number = issue_number
                issue_obj.issue_created_at = issue.created_at
                issue_obj.issue_url = issue.url
                issue_obj.state = issue.state
                issue_assignees = issue.assignees
                if issue_assignees:
                    all_issue_assignees.append((issue_number, issue_assignees))
                bulk_issue_objects.append(issue_obj)
    print(len(bulk_issue_objects))
    if bulk_issue_objects:
        GithubIssues.objects.bulk_create(bulk_issue_objects)
    print(all_issue_assignees)
    # if issue_assignees:
    #     assignees_names = [a.login for a in issue_assignees]
    #     assignees = GithubUsers.objects.filter(
    #         login_name__in=assignees_names)
