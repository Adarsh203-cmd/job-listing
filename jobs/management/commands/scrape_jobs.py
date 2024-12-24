from django.core.management.base import BaseCommand
from jobs.utils import fetch_and_save_jobs

class Command(BaseCommand):
    help = "Fetch jobs from the Adzuna API and save them to the database"

    def handle(self, *args, **kwargs):
        fetch_and_save_jobs()
