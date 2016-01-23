import sys
# from lib.scraper import PullAAAData
from django.core.management.base import BaseCommand, CommandError
from fuel_price.models import OilPrice
import os
import Quandl
class Command(BaseCommand):
    help = 'updat crude oil price'


    def handle(self, *args, **options):
        # trim_start="2001-12-31", trim_end="2005-12-31"
        # set start and end dates dynamically to match other data sources
        brent_save_price = "brent"
        start_date = "1998-3-1"
        end_date = "2015-11-1"
        api_req = Quandl.get('ODA/POILBRE_USD', trim_start=start_date,
         trim_end=end_date, collapse="monthly")
        data = api_req.to_dict()['Value']
        data_list = []
        for time_stamp, value in data.iteritems():
            year = time_stamp.year
            month = time_stamp.month
            data_list.append((time_stamp, value))
            # if year

        data_list_sorted = sorted(data_list)
        # for item in data_list_sorted:
        #     year = str(item[0].year)
        #     month = str(item[0].month)
        #     # print year, month
        #     # if year == start_year and month == start_month:
        #     #     print "data start index: %s" %(item[0])
        if OilPrice.objects.filter(oil_type=brent_save_price):
            brent = OilPrice.objects.get(oil_type=brent_save_price)
            brent.data = data_list_sorted
            brent.save()
            print "updating %s data points" %(len(data_list_sorted))
            print "starting point: %s" % data_list_sorted[0][0]
            print "end point: %s" % data_list_sorted[-1][0]
        else:
            print "saving %s data points" %(len(data_list_sorted))
            print "starting point: %s" % data_list_sorted[0][0]
            print "end point: %s" % data_list_sorted[-1][0]
            brent_crude = OilPrice(oil_type="brent")
            brent_crude.data = data_list_sorted
            brent_crude.save()
