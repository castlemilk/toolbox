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


        for state in states:
            json_data = AAA_data.xl_to_json(state)
            if json_data:
                for location, data in json_data.iteritems():

                    if AAAData.objects.filter(location=location):
                        location_data = AAAData.objects.get(state=state,
                                                        location=location)
                        location_data.data = data
                        location_data.save()
                        print "updating location: %s" % (location)
                    else:
                        location_data = AAAData(state=state, location=location)
                        location_data.data = data
                        location_data.save()
                        print "adding location: %s" % (location)
            else:
                print "no xl file found for state: %s" % state



        # self.stdout.write('There are {} things!'.format(AAAData.objects.count()))
