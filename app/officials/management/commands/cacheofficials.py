import os
import requests
from django.core.management.base import BaseCommand

from officials.models import ElectionRegion, ElectionOffice, OfficeFunction


class Command(BaseCommand):
    help = "Cache election official information from external API"
    requires_system_checks = False

    def add_arguments(self, parser):
        parser.add_argument(
            "--api-url",
            nargs=1,
            type=str,
            default=["https://api.usvotefoundation.org/eod/v3/"],
            help="API to import from, defaults to US Vote Foundation",
        )
        parser.add_argument(
            "--api-key",
            nargs=1,
            type=str,
            default=[os.environ.get("USVF_API_KEY", None)],
            help="API Key",
        )
        parser.add_argument(
            "--limit",
            nargs=1,
            type=int,
            default=[20,],
            help="Limit number of objects pulled from API in one request",
        )
        parser.add_argument(
            "--total",
            nargs=1,
            type=int,
            default=[100,],
            help="Total number of objects pulled from API",
        )

    def handle(self, *args, **options):
        API_URL = options["api_url"][0]
        API_KEY = options["api_key"][0]
        TOTAL_OBJECTS = options["total"][0]

        session = requests.Session()
        session.headers.update({
            'Authorization': f'OAuth {API_KEY}'
        })
        session.params.update({
            'limit': options["limit"][0]
        })

        num_objects = 0
        regions = session.get(f"{API_URL}/regions/").json()

        for region in regions['objects']:
            # get_or_create Region based on external_id

            # request office from api with external_id

            # get_or_create ElectionOffice

            # find first address with is_regular_mail=True

            # store mailing address, main contact info

            # find first address with is_physical=True

            # geocode and store lat/lon

            # increment num_objects

            # check to see if we are over total

            
