import sys
from lib.scraper import PullAAAData
# from lib.scraper import PullAAAData
from django.core.management.base import BaseCommand, CommandError
from fuel_price.models import AAAData
import os
class Command(BaseCommand):
    help = 'Does some magical work'

    def handle(self, *args, **options):
        """ Do your work here """

        url = "http://www.aaa.asn.au/aaa-agenda/affordability/latest-fuel-prices/"
        states = ['vic',]
        # save_location = os.path.join(os.getcwd(),'management/data/scraper_data/aaa_site')
        save_location = os.path.join(os.getcwd(),
                'fuel_price/management/data/scraper_data/aaa_site')
        AAA_data = PullAAAData(url, states, save_location)

        json_data = AAA_data.xl_to_json()

        print json_data
        # self.stdout.write('There are {} things!'.format(AAAData.objects.count()))
