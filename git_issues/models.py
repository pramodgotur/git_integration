from django.db import models

# Create your models here.


class GithubUsers(models.Model):
    login_name = models.CharField(max_length=200)


class Lables(models.Model):
    name = models.CharField(max_length=100)


class GithubIssues(models.Model):
    title = models.CharField(max_length=500)
    issue_number = models.IntegerField(db_index=True)
    assignees = models.ManyToManyField(
        GithubUsers, on_delete=models.CASCADE, related_name="issue_assignees")
    lables = models.ManyToManyField(
        GithubUsers, on_delete=models.CASCADE, related_name="issue_lables")
    issue_created_at = models.DatetimeField()
    issue_url = models.CharField(max_length=200)
