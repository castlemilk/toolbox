import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse, urljoin, urlsplit
import re
import os
import time
import sys
# from ..fuel_price import models
# from django.conf import settings
# settings.configure()

class PullAAAData(object):
    class Meta:
        url = "http://www.aaa.asn.au/aaa-agenda/affordability/latest-fuel-prices/"
        state_pattern = re.compile('-(?P<state>[a-z]+).xls')
        states = ['vic',]
        save_location = os.path.join(os.getcwd(),'management/data/scraper_data/aaa_site')
        print save_location

    def __init__(self, url, states, save_location, *args, **kw):
        super(PullAAAData, self).__init__(*args, **kw)
        self.url = url
        self.states = states
        self.save_location = save_location
        self.HTML = None
        self.HTML_parsed = None
        self.download_links = {}
        self.links = {}
        self.parsed_uri = urlparse(self.Meta.url)
        self.domain = '{uri.scheme}://{uri.netloc}/'.format(uri=self.parsed_uri)
        if not os.path.exists(self.save_location):
            print "save file doesnt exist, making now"
            os.makedirs(self.save_location)



    def get_site_html(self):
        request = urllib2.Request(self.url)
        response = urllib2.urlopen(request)
        self.HTML = response.read()
        return self.HTML

    def parse_html(self):
        if self.HTML:
            self.HTML_parsed = BeautifulSoup(self.HTML, 'html.parser')
            return HTML_parsed
        else:
            self.HTML = self.get_site_html()
            self.HTML_parsed = BeautifulSoup(self.HTML, 'html.parser')
            return self.HTML_parsed

    def get_links(self):
        self.parse_html()
        site_links = self.HTML_parsed.find("map")
        for link in site_links:
            if link !='\n':
                link_directory = link.get("href")
                # eg look for 'vic' in 'storage/xx-vic.xls'
                m = re.search(self.Meta.state_pattern, link_directory)
                if m:
                    self.links[
                    m.groupdict()['state']] = urljoin(
                                                        self.domain,
                                                        link_directory
                                                              )


        return self.links


    def get_download_links(self):
        self.get_links()
        # for state, link in self.links.iteritems():
        #     if state in self.Meta.states:
        #         self.download_links[state] = link
        for state in self.states:
            self.download_links[state] = {}
            try:
                self.download_links[state]['link'] = self.links[state]
            except:
                print "failed to set link for state %s" % (state)
                self.download_links[state]['link'] = ['NA']
            try:
                self.download_links[state]['file_name'] = os.path.basename(
                                            urlsplit(self.links[state]).path)
            except:
                print "failed to set file_name for %s " % (state)
                self.download_links[state]['file_name'] = []
            try:
                self.download_links[state]['file_type'] = os.path.splitext(
                            os.path.basename(urlsplit(self.links[state]).path)
                                                                      )[1]
            except:
                print "couldnt find a type for file"


        return self.download_links

    def download(self):
        self.get_download_links()
        for key, items in self.download_links.iteritems():
            print "downloading %s file [%s] from %s" % (
                                                    items['file_type'],
                                                    items['file_name'],
                                                    items['link'])
            save_as = os.path.join(self.save_location, items['file_name'])
            print "saving as %s" % (save_as)
            scraper_lib.download_url(items['link'], save_as)



    def xl_to_json(self, state):
        from xlrd import open_workbook,xldate_as_tuple
        import json
        try:
            state_file = next(file for file in os.listdir(self.save_location) if state in file)
        except StopIteration, e:
            print "no file found for %s " % (state)
        if state_file:
                xl_file_directory = os.path.join(self.save_location, state_file)
                print "loading working from %s" % (xl_file_directory)

                book = open_workbook(xl_file_directory)
                sheet = book.sheet_by_index(0)
                key_cols = [sheet.cell(4,col_index).value for col_index in
                xrange(sheet.ncols)]
                dates_clean = []
                for date in key_cols:
                    if date != '':
                        dates_clean.append(xldate_as_tuple(date, book.datemode))
                location_column = [sheet.cell(row_index, 0).value.strip() for row_index
                in xrange(6,sheet.nrows-7)]
                variables_column = [sheet.cell(row_index, 1).value.strip() for row_index
                in xrange(6,sheet.nrows-7)]

                data = {}

                # initialise data block
                for row in location_column:
                    if row != '':
                        data[row] = {}

                for row_index,location in enumerate(location_column):
                    if location != '' and variables_column[row_index] != '':
                        data[location][variables_column[row_index]] = [
                        sheet.cell(row_index+6,col_index).value for col_index in
                        xrange(2,sheet.ncols)]

                return data















    # using urllib2
    # f = urllib2.urlopen(url)
    # data = f.read()
    # with open(save_location, "wb") as f:
    #     f.write(data)

    # HTTP request
    # r = requests.get(url)
    # with open(save_location, "wb") as f:
    #     f.write(r.content)
