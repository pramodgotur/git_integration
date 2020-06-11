from django.conf import settings
from github import Github
GITHUB_REPO = settings.GITHUB_REPO


def get_gitobject():
    gitobj = Github(per_page=100)
    return gitobj


def get_repo():
    gitobj = get_gitobject()
    return gitobj.get_repo(GITHUB_REPO)


def get_issues(repo, state="open"):
    issues = repo.get_issues(state=state)
    return issues


def get_labels(repo):
    lables = repo.get_labels()
    return lables
