from django.core.management.base import BaseCommand

from official.scraper import scrape


class Command(BaseCommand):
    help = "Cache election official information from external API"
    requires_system_checks = False

    def handle(self, *args, **options):
        scrape()
