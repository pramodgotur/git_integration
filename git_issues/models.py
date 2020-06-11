from django.db import models

# Create your models here.


class GithubUsers(models.Model):
    login_name = models.CharField(max_length=200)

    def __str__(self):
        return f'GithubUsers(login="{self.login_name}")'


class Labels(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Labels(name="{self.name}")'


class GithubIssues(models.Model):
    STATE_CHOICES = (
        ('open', 'open'),
        ('closed', 'closed'),
    )
    title = models.CharField(max_length=500)
    issue_number = models.IntegerField(db_index=True)
    assignees = models.ManyToManyField(
        GithubUsers, related_name="issue_assignees", blank=True)
    labels = models.ManyToManyField(
        GithubUsers, related_name="issue_labels", blank=True)
    issue_created_at = models.DateTimeField()
    state = models.CharField(max_length=30, choices=STATE_CHOICES)
    issue_url = models.CharField(max_length=200)

    def __str__(self):
        return f'GithubIssues(title="{self.title}"   Number={self.issue_number})'
