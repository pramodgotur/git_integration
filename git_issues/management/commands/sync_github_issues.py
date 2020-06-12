from django.core.management.base import BaseCommand, CommandError
from git_issues.api_helper.sync_issues_to_db import sync_issues


class Command(BaseCommand):
    help = 'Sync Github issues and saves to DB'

    def handle(self, *args, **options):
        total_issue_synced = sync_issues()
        self.stdout.write(self.style.SUCCESS(
            f'{total_issue_synced} issues synced'))
